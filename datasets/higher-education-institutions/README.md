# Tertiary and TVET institutions and programmes in Uganda

Universities, other tertiary institutions and technical and vocational (TVET) providers on the registers of NCHE, the TVET Council and the Ministry of Education and Sports, with their accredited programmes and a dated record of how each register has changed since April 2025.

## Data

| File | What it holds | Rows |
|---|---|---:|
| [`data/institutions.csv`](data/institutions.csv) | Every institution on the NCHE, TVET Council or Ministry TVET register since 2025-04-12, listed or not, with its current regulator, location and, for universities, website and email domain. See listings.csv for each register's own record. | 626 |
| [`data/listings.csv`](data/listings.csv) | One row per institution per register (nche, tvet-council, moes-tvet), with the register's own id, category, status and the first and last dates an import saw it. | 652 |
| [`data/programmes.csv`](data/programmes.csv) | Programmes on the NCHE and TVET Council registers, including ones no longer listed (see last_seen_on). | 4,629 |
| [`data/register-changes.csv`](data/register-changes.csv) | Institutions and programmes added to, dropped from or returning to a register, dated by the import that first saw the change. | 174 |
| [`data/register-snapshots.csv`](data/register-snapshots.csv) | Counts per register and import date, by dimension, for time series. Long format: one row per register, date, measure, dimension and value. | 98 |

Columns are described in [`datapackage.json`](datapackage.json). Ids are the portal's own ids: they are stable and never reused, and the `*_id` columns link to the units in [`administrative-units`](../administrative-units).

## Source

[NCHE, TVET Council and Ministry of Education and Sports](https://unche.or.ug), 2026-07-16.

## Notes

- Three regulators publish who may train students. The National Council for Higher Education (NCHE, unche.or.ug) licenses universities and other tertiary institutions and accredits their programmes. The Technical and Vocational Education and Training Act, 2025, in force since 15 March 2025, moved the licensing of TVET providers and the accreditation of TVET programmes to a new TVET Council (tvetcs.go.ug), which publishes the private providers it has licensed. The Ministry of Education and Sports TVET department (tvet.go.ug) lists the government and registered TVET institutions it runs.
- The two regulators' mandates overlap and NCHE has said the split is not settled: some institutions appear on both an NCHE and a TVET register, and NCHE marks programmes that lean towards TVET (tvetLeaning). This dataset keeps one record per institution and, separately, how each register lists it, so both views can be compared.
- Each register is read on the first Monday of every month. When an institution or programme appears on, disappears from or returns to a register, the change is recorded with the date of the read that first saw it. An institution dropped by NCHE and listed by a TVET register has moved between regulators; the date is when this portal noticed, not when the regulator decided. The first record is the NCHE website as scraped on 12 April 2025.
- Of the 321 institutions NCHE listed in April 2025, 141 were no longer on its register in November 2026. Eight of them now appear on a TVET register; most others are university campuses, public health training schools and military colleges that neither published TVET list includes.

## Known issues

- Institutions are matched across registers by name and curated aliases, so a renamed institution may appear twice until an alias is added.
- NCHE institutions are located to district level; Ministry TVET institutions to parish level where the parish name matches.
- The TVET Council publishes private providers only; government TVET institutions come from the Ministry register, which lists no programmes.
- Change dates are the dates of the monthly reads, so a change is dated up to a month after it happened.
- Websites and email domains come from wkambale/Ug-Universities-Api (MIT licence, https://github.com/wkambale/Ug-Universities-Api) and cover universities only.

## Changes

- **2026-11-09**: NCHE register of 16 July 2026 with 3,703 accredited programmes, TVET Council and Ministry TVET registers, campuses, register history and monthly updates.
- **2026-11-09**: Website and email domain for 43 universities, from wkambale/Ug-Universities-Api (MIT).
- **2026-11-08**: API v1 and bulk downloads.
- **2025-04-12**: First publication from the NCHE website.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the source above and Uganda Open Data contributors.
