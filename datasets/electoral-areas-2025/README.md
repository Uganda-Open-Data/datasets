# Constituencies and electoral areas of Uganda, 2025

Electoral Commission constituencies and the electoral areas of directly elected district, municipality and sub-county councillors from the 2025 demarcation, linked to the districts, counties, sub-counties and parishes of this portal.

## Data

| File | What it holds | Rows |
|---|---|---:|
| [`data/constituencies.csv`](data/constituencies.csv) | Electoral Commission constituencies with the portal ids of their district and county. | 353 |
| [`data/electoral-areas.csv`](data/electoral-areas.csv) | One row per electoral area with its constituency and the portal ids of its sub-county and parish. | 13,331 |

Columns are described in [`datapackage.json`](datapackage.json). Ids are the portal's own ids: they are stable and never reused, and the `*_id` columns link to the units in [`administrative-units`](../administrative-units).

## Source

[Electoral Commission of Uganda: Display list of demarcated electoral areas for local government council elections 2025](https://www.ec.or.ug/info/lists-demarcated-electoral-areas-2025), 2025-01-01.

## Known issues

- Polling stations are not included: the Electoral Commission has not published a list of them in a usable form.
- Women councillor electoral areas (which group several areas) are not included.
- Constituencies are linked to the county of the same name; municipality constituencies are linked to the municipal council at district level, with no county.
- Electoral areas are linked by name to sub-counties and parishes; the Electoral Commission codes and names as published are kept.

## Changes

- **2026-11-08**: First publication: 353 constituencies and 13,331 electoral areas.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the source above and Uganda Open Data contributors.
