# Government primary and secondary schools in Uganda

Government primary schools (2016 list) and government secondary schools published by the Ministry of Education and Sports, with their EMIS numbers, linked to the district, sub-county and parish of this portal.

## Data

| File | What it holds | Rows |
|---|---|---:|
| [`data/schools.csv`](data/schools.csv) | One row per school with its EMIS number and the portal ids of its district, sub-county and parish. | 13,110 |

Columns are described in [`datapackage.json`](datapackage.json). Ids are the portal's own ids: they are stable and never reused, and the `*_id` columns link to the units in [`administrative-units`](../administrative-units).

## Source

[Ministry of Education and Sports: List of Government Primary Schools 2016; Government Secondary Schools](https://www.education.go.ug/?p=2501), 2017-11-06.

## Known issues

- Only government schools: the Ministry has not published a list of private and community schools in a usable form.
- The primary list dates from 2016. Schools opened, closed or renamed since then are not reflected.
- Schools are linked by the names of the district, sub-county and parish in the list. All are linked to a district, about 78% of primary schools to a sub-county and 71% to a parish; the names as listed are kept in listedLocation.
- Secondary schools are linked to their district only.
- The phone numbers in the primary list are personal contacts and are not published.

## Changes

- **2026-11-08**: First publication: 12,085 government primary and 1,025 government secondary schools.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the source above and Uganda Open Data contributors.
