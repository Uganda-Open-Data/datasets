"""Summarise the rows each pull request adds, removes and changes.

    python tools/diff_summary.py origin/main >> "$GITHUB_STEP_SUMMARY"

Rows are matched on each table's primaryKey (or the dataset's portal.key), so a changed
name shows as one changed row rather than one removed and one added.
"""

import csv
import io
import json
import subprocess
import sys
from pathlib import Path


def _rows(text: str, key: list[str]) -> dict[str, dict]:
    return {"|".join(row[field] for field in key): row for row in csv.DictReader(io.StringIO(text))}


def key_for(package: dict, path: str) -> list[str] | None:
    """The columns that identify a row of one table: its primaryKey, else portal.key."""
    for resource in package.get("resources", []):
        if resource.get("path") == path:
            key = resource.get("schema", {}).get("primaryKey") or package.get("portal", {}).get("key")
            return [key] if isinstance(key, str) else key
    return None


def summarise(old_csv: str | None, new_csv: str, key: list[str]) -> dict:
    old = _rows(old_csv, key) if old_csv is not None else {}
    new = _rows(new_csv, key)
    return {
        "added": len(new.keys() - old.keys()),
        "removed": len(old.keys() - new.keys()),
        "changed": sum(1 for k in new.keys() & old.keys() if new[k] != old[k]),
    }


def render(rows: list[tuple[str, dict]]) -> str:
    if not rows:
        return "### Rows changed\n\nNo data files changed.\n"
    lines = ["### Rows changed", "", "| File | Added | Changed | Removed |", "|---|---:|---:|---:|"]
    lines += [f"| `{path}` | {c['added']} | {c['changed']} | {c['removed']} |" for path, c in rows]
    return "\n".join(lines) + "\n"


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def main(base_ref: str) -> int:
    changed = _git("diff", "--name-only", f"{base_ref}...HEAD", "--", "datasets/*/data/*.csv").split()
    rows = []
    for path in changed:
        file = Path(path)
        if not file.exists():
            continue
        package = json.loads((file.parent.parent / "datapackage.json").read_text(encoding="utf-8"))
        key = key_for(package, str(file.relative_to(file.parent.parent)))
        if not key:
            continue
        try:
            old = _git("show", f"{base_ref}:{path}")
        except subprocess.CalledProcessError:
            old = None
        rows.append((path, summarise(old, file.read_text(encoding="utf-8"), key)))
    print(render(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
