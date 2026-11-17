"""Check every dataset folder under datasets/.

Each dataset must be a valid Frictionless Data Package and follow the rules
in CONTRIBUTING.md: a slug that matches its folder, an accepted licence,
dated public sources, a portal block, unique row keys and no personal data.

    python tools/check.py                  check every dataset
    python tools/check.py --base ../base   also fail when a dataset folder
                                           in that checkout was removed
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from frictionless import validate

SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED = ["name", "title", "description", "version", "licenses", "sources", "resources", "portal"]
REQUIRED_PORTAL = ["theme", "keywords", "changelog", "key"]
LICENCES = {"CC0-1.0", "PDDL-1.0", "CC-BY-4.0", "ODC-BY-1.0"}
NEEDS_APPROVAL = {"ODbL-1.0", "CC-BY-SA-4.0"}
WARN_BYTES = 20 * 1024 * 1024
MAX_BYTES = 50 * 1024 * 1024

# Checked on each cell with spaces and dashes removed.
PHONE = re.compile(r"(?<!\d)(?:\+?256|0)7\d{8}(?!\d)")
# National ID numbers: CM (male) or CF (female) and 12 letters or digits.
NATIONAL_ID = re.compile(r"(?<![A-Z0-9])C[MF](?=[0-9A-Z]*\d)[0-9A-Z]{12}(?![A-Z0-9])")
PERSONAL_EMAIL = re.compile(r"[\w.+-]+@(?:gmail|yahoo|hotmail|outlook|ymail|live)\.[a-z.]+", re.IGNORECASE)


def check_package(folder: Path) -> list[str]:
    """The errors in one dataset folder, each starting with the folder name."""
    errors = [f"{folder.name}: {error}" for error in _package_errors(folder)]
    return errors


def _package_errors(folder: Path):
    path = folder / "datapackage.json"
    if not path.is_file():
        yield "datapackage.json is missing"
        return

    try:
        package = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        yield f"datapackage.json is not valid JSON: {error}"
        return

    if not SLUG.match(folder.name):
        yield f"folder {folder.name} is not a valid slug (lowercase words joined by hyphens)"
    if package.get("name") != folder.name:
        yield f"name '{package.get('name')}' does not match the folder"

    for key in REQUIRED:
        if key not in package:
            yield f"{key} is missing"

    portal = package.get("portal", {})
    for key in REQUIRED_PORTAL:
        if key not in portal:
            yield f"portal.{key} is missing"

    for licence in package.get("licenses", []):
        name = licence.get("name")
        if name in NEEDS_APPROVAL and not portal.get("licenceApprovedBy"):
            yield f"licence {name} needs portal.licenceApprovedBy (share-alike licences need a maintainer's approval)"
        elif name not in LICENCES | NEEDS_APPROVAL:
            yield f"licence {name} is not allowed (use one of {', '.join(sorted(LICENCES))})"

    for i, source in enumerate(package.get("sources", [])):
        if not source.get("path") or not DATE.match(str(source.get("date", ""))):
            yield f"sources[{i}] needs a path and a date (YYYY-MM-DD)"

    dates = [entry.get("date", "") for entry in portal.get("changelog", [])]
    if not all(DATE.match(str(date)) for date in dates):
        yield "portal.changelog dates must be YYYY-MM-DD"
    elif dates != sorted(dates, reverse=True):
        yield "portal.changelog must be newest first"

    resources_ok = True
    for i, resource in enumerate(package.get("resources", [])):
        file = folder / str(resource.get("path", ""))
        if not str(resource.get("path", "")).startswith("data/") or not file.is_file():
            resources_ok = False
            yield f"resources[{i}] path {resource.get('path')} must be a file under data/"
            continue

        size = file.stat().st_size
        if size > MAX_BYTES:
            yield f"{file.name} is {size // 1024 // 1024} MB; files over 50 MB go in release assets"
        elif size > WARN_BYTES:
            print(f"warning: {folder.name}: {file.name} is {size // 1024 // 1024} MB", file=sys.stderr)

        if "key" in portal:
            yield from _duplicate_keys(file, portal["key"])
        yield from scan_personal_data(file)

    if resources_ok:
        yield from _frictionless_errors(path)


def _duplicate_keys(file: Path, key: list[str]):
    seen: dict[str, int] = {}
    with file.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in key if field not in (reader.fieldnames or [])]
        if missing:
            yield f"{file.name} has no column {', '.join(missing)} named in portal.key"
            return
        for row_number, row in enumerate(reader, start=2):
            value = "|".join(row[field] for field in key)
            if value in seen:
                yield f"{file.name} has the duplicate key {value} on rows {seen[value]} and {row_number}"
            else:
                seen[value] = row_number


def _frictionless_errors(path: Path):
    report = validate(str(path))
    for task in report.tasks:
        name = Path(task.name or task.place).name
        for error in task.errors:
            where = []
            if getattr(error, "row_number", None):
                where.append(f"row {error.row_number}")
            if getattr(error, "field_name", None):
                where.append(error.field_name)
            yield f"{name} {' '.join(where)}: {error.message}".replace("  ", " ")
    for error in report.errors:
        yield error.message


def scan_personal_data(csv_path: Path) -> list[str]:
    """Cells that look like phone numbers, national ID numbers or personal email addresses."""
    errors = []
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row_number, row in enumerate(reader, start=2):
            for column, value in row.items():
                if not value:
                    continue
                problem = None
                if PHONE.search(re.sub(r"[\s\-]", "", value)):
                    problem = "phone number"
                elif NATIONAL_ID.search(value):
                    problem = "national ID number"
                elif PERSONAL_EMAIL.search(value):
                    problem = "personal email address"
                if problem:
                    errors.append(f"{csv_path.name} row {row_number} {column}: looks like a {problem}")
    return errors


def removed_datasets(base: set[str], head: set[str]) -> set[str]:
    """Datasets in the base checkout that are gone now. Slugs never change once released."""
    return base - head


def _folders(root: Path) -> list[Path]:
    return sorted(path for path in root.iterdir() if path.is_dir()) if root.is_dir() else []


def main(root: Path = Path("datasets"), base: Path | None = None) -> int:
    errors = [error for folder in _folders(root) for error in check_package(folder)]

    if base is not None:
        gone = removed_datasets({p.name for p in _folders(base)}, {p.name for p in _folders(root)})
        errors += [f"{name}: the dataset folder was removed or renamed; released slugs never change" for name in sorted(gone)]

    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", type=Path, help="datasets/ folder of the branch a pull request goes into")
    args = parser.parse_args()
    sys.exit(main(base=args.base))
