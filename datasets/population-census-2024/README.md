# Population and households of Uganda by parish, 2024 census

Population by sex, household population, number of households and average household size for districts, counties, sub-counties and parishes, from the UBOS National Population and Housing Census 2024 sub-region profile reports, linked to the administrative units in this portal.

## Data

| File | What it holds | Rows |
|---|---|---:|
| [`data/population.csv`](data/population.csv) | One row per district, county, sub-county or parish with its 2024 census figures. | 12,321 |

Columns are described in [`datapackage.json`](datapackage.json). Ids are the portal's own ids: they are stable and never reused, and the `*_id` columns link to the units in [`administrative-units`](../administrative-units).

## Source

[Uganda Bureau of Statistics (UBOS), National Population and Housing Census 2024, sub-region profile reports (Volume 2)](https://statistics.ubos.org/nphc/report?cat=reports), 2025-06-01.

## Known issues

- Figures were extracted from the UBOS PDF reports. A table was kept only where every parent equals the sum of its children; about a dozen district tables (or parts of them) failed that check and are left out.
- Census names are matched to portal units by name within their parent. Units the portal has under a different name or parent, and new units, have no figures (about 8% of parishes).
- UBOS district figures include the municipalities inside the district; the portal lists municipal councils separately, with their own figures.
- Where the portal has the same place twice, the figures go to the entry with the most children.

## Changes

- **2026-11-08**: First publication: population by sex and households for districts, counties, sub-counties and parishes.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the source above and Uganda Open Data contributors.
