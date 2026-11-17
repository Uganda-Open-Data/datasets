# Uganda Open Data: datasets

Open data about Uganda, one folder per dataset, in CSV with a
[Frictionless Data Package](https://datapackage.org/) (`datapackage.json`)
that describes every column, the sources and the licence.

The Uganda OpenData Playground portal loads tagged releases of this
repository; its pages, API and bulk downloads are built from these files.
Anyone can read, use, correct or add to the data.

## Datasets

| Dataset | Folder | Source | Licence |
|---|---|---|---|
| Government and diplomatic number plate codes | [`datasets/registration-plates`](datasets/registration-plates) | Ministry of Works and Transport, 2024 schedule | CC-BY-4.0 |

## Using the data

- **Releases:** each [release](https://github.com/Uganda-Open-Data/datasets/releases)
  has a tarball of every dataset and a `SHA256SUMS` file. Releases are
  numbered `0.1`, `0.2`, … and never change once published. A dataset's
  `version` in its `datapackage.json` is the release that last changed it.
- **Single files:** read a CSV straight from GitHub at a release tag, e.g.
  `https://raw.githubusercontent.com/Uganda-Open-Data/datasets/<release>/datasets/registration-plates/data/registration_plate_codes.csv`.
- **With Frictionless:** `datapackage.json` loads directly in
  [frictionless-py](https://github.com/frictionlessdata/frictionless-py),
  R `frictionless` and other Data Package tools, with column types applied.

## Licences

- The data and the documentation are licensed under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (see `LICENSE`),
  unless a dataset's `datapackage.json` names another licence its source
  requires.
- The checks in `tools/` and the workflows in `.github/` are MIT licensed
  (see `tools/LICENSE`).

When you use the data, credit it as:

> Uganda Open Data contributors, https://github.com/Uganda-Open-Data/datasets (CC BY 4.0)

and credit the original sources listed in each dataset's `datapackage.json`.

## Contributing

Corrections and new datasets are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md);
small fixes can be made in the browser without installing anything. Everyone
taking part follows the [code of conduct](CODE_OF_CONDUCT.md).
