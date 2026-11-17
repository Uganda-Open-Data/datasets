import json
from pathlib import Path

import pytest


def write_package(root: Path, folder_name: str = "example", rows: str | None = None, **changes) -> Path:
    """Write a small valid dataset folder, then apply changes to its datapackage.json."""
    folder = root / folder_name
    (folder / "data").mkdir(parents=True)
    (folder / "data" / "rows.csv").write_text(
        rows if rows is not None else "scheme,code,name,website,note\n2024,01,Office of the President,https://op.go.ug/,\n2024,02,Education Service Commission,,\n"
    )
    package = {
        "name": folder_name,
        "title": "Example",
        "description": "An example dataset.",
        "version": "2026.11.18",
        "licenses": [{"name": "CC-BY-4.0", "path": "https://creativecommons.org/licenses/by/4.0/", "title": "Creative Commons Attribution 4.0 International"}],
        "sources": [{"title": "Example source", "path": "https://example.org/", "date": "2025-01-01"}],
        "portal": {
            "theme": "Transport",
            "keywords": ["Uganda"],
            "changelog": [{"date": "2026-11-16", "note": "Second."}, {"date": "2026-11-13", "note": "First."}],
            "key": ["scheme", "code"],
        },
        "resources": [{
            "name": "rows",
            "path": "data/rows.csv",
            "schema": {"fields": [
                {"name": "scheme", "type": "string", "constraints": {"required": True}},
                {"name": "code", "type": "string"},
                {"name": "name", "type": "string", "constraints": {"required": True}},
                {"name": "website", "type": "string", "format": "uri"},
                {"name": "note", "type": "string"},
            ]},
        }],
    }
    for path, value in changes.items():
        target = package
        *parents, last = path.split("__")
        for key in parents:
            target = target[int(key)] if isinstance(target, list) else target[key]
        if value is None:
            target.pop(last, None) if isinstance(target, dict) else None
        elif isinstance(target, list):
            target[int(last)] = value
        else:
            target[last] = value
    (folder / "datapackage.json").write_text(json.dumps(package, indent=2))
    return folder


@pytest.fixture
def package(tmp_path):
    return lambda **kwargs: write_package(tmp_path, **kwargs)
