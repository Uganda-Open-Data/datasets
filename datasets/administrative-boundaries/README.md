# Administrative boundaries of Uganda

Boundary polygons of the regions, sub-regions, districts and cities, counties, sub-counties and parishes of Uganda, joined to the units of this portal by their UBOS codes, with a bounding box, centroid and area for each. Processed from the Uganda Bureau of Statistics 2024 census boundaries and the Electoral Commission 2025 boundaries by the uganda-locale project.

## Data

| File | What it holds | Rows |
|---|---|---:|
| [`data/regions.geojson`](data/regions.geojson) | GeoJSON polygons (WGS 84) of the regions. Each feature's properties: id (the portal id), type, level, name, displayName, slug, ubosCode, areaKm2, centroid, inferred and links. Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data. | 4 |
| [`data/sub-regions.geojson`](data/sub-regions.geojson) | GeoJSON polygons (WGS 84) of the sub-regions. Each feature's properties: id (the portal id), type, level, name, displayName, slug, ubosCode, areaKm2, centroid, inferred and links. Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data. | 11 |
| [`data/districts.geojson`](data/districts.geojson) | GeoJSON polygons (WGS 84) of the districts. Each feature's properties: id (the portal id), type, level, name, displayName, slug, ubosCode, areaKm2, centroid, inferred and links. Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data. | 177 |
| [`data/counties.geojson`](data/counties.geojson) | GeoJSON polygons (WGS 84) of the counties. Each feature's properties: id (the portal id), type, level, name, displayName, slug, ubosCode, areaKm2, centroid, inferred and links. Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data. | 320 |
| [`data/sub-counties.geojson`](data/sub-counties.geojson) | GeoJSON polygons (WGS 84) of the sub-counties. Each feature's properties: id (the portal id), type, level, name, displayName, slug, ubosCode, areaKm2, centroid, inferred and links. Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data. | 2,133 |
| [`data/parishes.geojson`](data/parishes.geojson) | GeoJSON polygons (WGS 84) of the parishes. Each feature's properties: id (the portal id), type, level, name, displayName, slug, ubosCode, areaKm2, centroid, inferred and links. Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data. | 10,596 |
| [`data/centroids.csv`](data/centroids.csv) | One row per unit that has a boundary polygon, joined to the other datasets by unit_type and unit_id. Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data. | 13,241 |

Columns are described in [`datapackage.json`](datapackage.json). Ids are the portal's own ids: they are stable and never reused, and the `*_id` columns link to the units in [`administrative-units`](../administrative-units).

## Source

[uganda-locale project (CC BY 4.0)](https://github.com/kakandemanwell/uganda), 2026-11-04.

Also drawn from:

- [Uganda Bureau of Statistics (UBOS), National Population and Housing Census 2024 boundaries](https://www.ubos.org)
- [Electoral Commission of Uganda, 2025 electoral area boundaries](https://www.ec.or.ug)
- [OCHA Common Operational Datasets (P-codes)](https://data.humdata.org/dataset/cod-ab-uga)

When you use this data, show: Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data.

## Notes

- The polygons are processed data, not an official UBOS release: the uganda-locale project assembled them from the UBOS 2024 census boundaries (districts and sub-counties) and the Electoral Commission 2025 boundaries (parishes), simplified to 5 decimal places (about 1 metre).
- Units are joined to the polygons by their full UBOS code (district, county, sub-county and parish codes together), and by name within their district or sub-county where the codes differ, such as in Kampala and in town councils created recently.
- Coordinates are WGS 84 longitude and latitude (EPSG:4326), as in every GeoJSON file. The centroid is the centre of area, which can fall outside a curved or split unit.
- Use and share the polygons under CC BY 4.0 with this credit: Boundaries: uganda-locale project (github.com/kakandemanwell/uganda, CC BY 4.0), processed from Uganda Bureau of Statistics NPHC 2024 and Electoral Commission 2025 data.

## Known issues

- Villages have no polygons: no open source has them. Village pages show the parish they lie in.
- About 2% of parishes and 4% of sub-counties have no polygon, mostly town councils, wards and town boards created after the source boundaries were drawn. "php artisan opendata:import-boundaries -v" lists them.
- The source drew 73 parishes and 3 sub-counties from the land left over between their neighbours; these are marked inferred.
- Sub-regions are matched by name: Buganda North, Buganda South, Elgon and Greater Kampala are grouped differently in the source and have no polygon of their own. Their maps show their districts.
- Kampala Capital City Authority divisions are counties in this portal but sub-counties in the source, so they have polygons as sub-counties only.

## Changes

- **2026-11-10**: First publication: polygons from region to parish, read from the uganda-locale project at commit bb3ee6b.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the source above and Uganda Open Data contributors.
