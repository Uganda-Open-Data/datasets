from tools.diff_summary import render, summarise

OLD = "code,name\nA,One\nB,Two\nC,Three\n"
NEW = "code,name\nA,One\nB,Deux\nD,Four\n"


def test_counts_rows_added_removed_and_changed():
    assert summarise(OLD, NEW, ["code"]) == {"added": 1, "removed": 1, "changed": 1}


def test_a_new_file_counts_every_row_as_added():
    assert summarise(None, NEW, ["code"]) == {"added": 3, "removed": 0, "changed": 0}


def test_render_makes_a_markdown_table():
    table = render([("datasets/x/data/rows.csv", {"added": 1, "removed": 0, "changed": 2})])
    assert "| `datasets/x/data/rows.csv` | 1 | 2 | 0 |" in table
    assert table.startswith("### Rows changed")


def test_render_says_when_no_data_changed():
    assert "No data files changed" in render([])


def test_key_for_uses_the_table_primary_key_then_portal_key():
    from tools.diff_summary import key_for

    package = {"portal": {"key": ["scheme"]}, "resources": [
        {"path": "data/a.csv", "schema": {"primaryKey": ["id"]}},
        {"path": "data/b.csv", "schema": {}},
    ]}
    assert key_for(package, "data/a.csv") == ["id"]
    assert key_for(package, "data/b.csv") == ["scheme"]
    assert key_for(package, "data/c.csv") is None
