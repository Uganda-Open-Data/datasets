# Administrative units of Uganda

The administrative hierarchy of Uganda from regions down to villages: 4 regions, 15 sub-regions, districts (including cities and municipal councils), counties, sub-counties, parishes and villages, with the codes used by government and a crosswalk to ISO 3166-2, OCHA COD-AB P-codes, Wikidata, OpenStreetMap and GeoNames.

## Data

| File | What it holds | Rows |
|---|---|---:|
| [`data/regions.csv`](data/regions.csv) | All Regions with the ids of their ancestors. | 4 |
| [`data/sub-regions.csv`](data/sub-regions.csv) | All Sub-regions with the ids of their ancestors. | 15 |
| [`data/districts.csv`](data/districts.csv) | All Districts with the ids of their ancestors. | 178 |
| [`data/counties.csv`](data/counties.csv) | All Counties with the ids of their ancestors. | 353 |
| [`data/sub-counties.csv`](data/sub-counties.csv) | All Sub-counties with the ids of their ancestors. | 2,219 |
| [`data/parishes.csv`](data/parishes.csv) | All Parishes with the ids of their ancestors. | 10,765 |
| [`data/villages.csv`](data/villages.csv) | All Villages with the ids of their ancestors. | 71,679 |
| [`data/changes.csv`](data/changes.csv) | Every recorded change: created, renamed, recoded, moved, retired, reinstated, deleted, split or merged. | 0 |

Columns are described in [`datapackage.json`](datapackage.json). Ids are the portal's own ids: they are stable and never reused; `parent_id` and the other `*_id` columns link the levels.

## Source

[Uganda Bureau of Statistics (UBOS)](https://www.ubos.org), 2025-04-10.

## Known issues

- Codes (ubosCode) are only unique within their parent unit, except for districts. Use the numeric id as the identifier.
- Cities and municipal councils appear as separate units at district level.
- UBOS district codes are not ISO 3166-2 codes; the ISO code is published separately in the identifiers attribute.
- COD-AB P-codes are matched by name against the 2020 COD-AB boundaries. Cities, divisions and units created or reorganised since 2020 may have no P-code.
- 70 villages have no household code prefix (hh_code_prefix). Run "php artisan opendata:validate" for the current list of data quality warnings.
- The change history starts on 2026-11-08; earlier boundary changes (such as the 2020 cities) are not recorded, and validity dates are empty unless known.

## Changes

- **2026-11-08**: Validity dates and a change history for every unit; retired units drop out of lists but stay available. Crosswalk to COD-AB P-codes, Wikidata, OpenStreetMap and GeoNames.
- **2026-11-08**: API v1: stable ids, full ancestor path, ISO 3166-2 crosswalk, bulk downloads.
- **2025-04-10**: First publication.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the source above and Uganda Open Data contributors.
