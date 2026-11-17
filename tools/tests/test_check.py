from tools.check import check_package, main, removed_datasets, scan_personal_data


def test_valid_package_has_no_errors(package):
    assert check_package(package()) == []


def test_folder_must_match_name(package):
    folder = package(folder_name="bad-name", **{"name": "other"})
    assert "bad-name: name 'other' does not match the folder" in check_package(folder)


def test_slug_must_be_lowercase_kebab_case(package):
    folder = package(folder_name="Bad_Name")
    assert any("not a valid slug" in e for e in check_package(folder))


def test_missing_portal_keys_are_reported(package):
    folder = package(**{"portal__key": None})
    assert "example: portal.key is missing (or give every table a schema.primaryKey)" in check_package(folder)


def test_licence_outside_allow_list_is_refused(package):
    folder = package(**{"licenses__0": {"name": "CC-BY-NC-4.0"}})
    assert any("licence CC-BY-NC-4.0 is not allowed" in e for e in check_package(folder))


def test_share_alike_needs_approval(package):
    folder = package(**{"licenses__0": {"name": "ODbL-1.0"}})
    assert any("ODbL-1.0 needs portal.licenceApprovedBy" in e for e in check_package(folder))


def test_approved_share_alike_passes(package):
    folder = package(**{"licenses__0": {"name": "ODbL-1.0"}, "portal__licenceApprovedBy": "ssmusoke"})
    assert check_package(folder) == []


def test_source_needs_path_and_date(package):
    folder = package(**{"sources__0__date": None})
    assert "example: sources[0] needs a path and a date (YYYY-MM-DD)" in check_package(folder)


def test_changelog_must_be_newest_first(package):
    folder = package(**{"portal__changelog": [{"date": "2026-11-13", "note": "First."}, {"date": "2026-11-16", "note": "Second."}]})
    assert "example: portal.changelog must be newest first" in check_package(folder)


def test_resource_must_live_in_data_and_exist(package):
    folder = package(**{"resources__0__path": "rows.csv"})
    assert any("resources[0] path rows.csv must be a file under data/" in e for e in check_package(folder))


def test_duplicate_key_is_reported_with_both_rows(package):
    folder = package(rows="scheme,code,name,website,note\n2024,38,Works,,\n2024,38,Works again,,\n")
    assert "example: rows.csv has the duplicate key 2024|38 on rows 2 and 3" in check_package(folder)


def test_empty_values_count_as_part_of_the_key(package):
    folder = package(rows="scheme,code,name,website,note\n2024,,Police,,\n2025,,Prisons,,\n")
    assert check_package(folder) == []


def test_frictionless_type_errors_are_reported(package):
    folder = package(rows="scheme,code,name,website,note\n2024,01,Office,not a url,\n")
    assert any("website" in e and "row 2" in e for e in check_package(folder))


def test_phone_number_in_any_column_fails(package):
    folder = package(rows="scheme,code,name,website,note\n2024,01,Office,,Call 0772 123 456\n")
    assert scan_personal_data(folder / "data" / "rows.csv") == ["rows.csv row 2 note: looks like a phone number"]


def test_international_phone_number_fails(package):
    folder = package(rows="scheme,code,name,website,note\n2024,01,Office,,+256-701-234567\n")
    assert scan_personal_data(folder / "data" / "rows.csv") == ["rows.csv row 2 note: looks like a phone number"]


def test_national_id_number_fails(package):
    folder = package(rows="scheme,code,name,website,note\n2024,01,Office,,CM90012345678A\n")
    assert scan_personal_data(folder / "data" / "rows.csv") == ["rows.csv row 2 note: looks like a national ID number"]


def test_free_mail_address_fails_but_an_official_one_does_not(package):
    folder = package(rows="scheme,code,name,website,note\n2024,01,Office,,someone@gmail.com\n2024,02,Office,,info@op.go.ug\n")
    assert scan_personal_data(folder / "data" / "rows.csv") == ["rows.csv row 2 note: looks like a personal email address"]


def test_plate_numbers_and_codes_are_not_phone_numbers(package):
    folder = package(rows="scheme,code,name,website,note\n2024,01,Office,,UG 38 00012 and LG 139 0001\n")
    assert scan_personal_data(folder / "data" / "rows.csv") == []


def test_personal_data_makes_the_package_fail(package):
    folder = package(rows="scheme,code,name,website,note\n2024,01,Office,,0772123456\n")
    assert "example: rows.csv row 2 note: looks like a phone number" in check_package(folder)


def test_removed_dataset_is_reported():
    assert removed_datasets({"a", "b"}, {"a"}) == {"b"}


def test_main_returns_one_when_a_dataset_fails(tmp_path, package):
    package(folder_name="bad-name", **{"name": "other"})
    assert main(tmp_path) == 1


def test_main_returns_zero_when_every_dataset_passes(tmp_path, package):
    package()
    assert main(tmp_path) == 0


def test_main_fails_when_a_dataset_folder_was_removed(tmp_path, package):
    from tools.tests.conftest import write_package

    base = tmp_path / "base" / "datasets"
    head = tmp_path / "head" / "datasets"
    write_package(base, "kept")
    write_package(base, "gone")
    write_package(head, "kept")
    assert main(head, base=base) == 1


def _with_geojson(package, text):
    folder = package()
    (folder / "data" / "regions.geojson").write_text(text)
    import json
    descriptor = json.loads((folder / "datapackage.json").read_text())
    descriptor["resources"].append({"name": "regions", "path": "data/regions.geojson", "format": "geojson", "mediatype": "application/geo+json"})
    (folder / "datapackage.json").write_text(json.dumps(descriptor))
    return folder


def test_geojson_resources_pass_when_they_are_feature_collections(package):
    folder = _with_geojson(package, '{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"phone": "0772123456"}, "geometry": null}]}')
    assert check_package(folder) == []


def test_geojson_that_is_not_a_feature_collection_fails(package):
    folder = _with_geojson(package, '{"type": "Feature"}')
    assert "example: regions.geojson is not a GeoJSON FeatureCollection" in check_package(folder)


def test_geojson_that_is_not_json_fails(package):
    folder = _with_geojson(package, "not json")
    assert "example: regions.geojson is not a GeoJSON FeatureCollection" in check_package(folder)


def test_a_table_primary_key_replaces_portal_key(package):
    folder = package(rows="scheme,code,name,website,note\n2024,38,Works,,\n2025,38,Works,,\n", **{"portal__key": None, "resources__0__schema__primaryKey": ["code"]})
    errors = check_package(folder)
    assert "example: portal.key is missing" not in errors
    assert "example: rows.csv has the duplicate key 38 on rows 2 and 3" in errors
