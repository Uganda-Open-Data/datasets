# Contributing

Thank you for helping. Every change is a pull request that the checks in
`tools/` validate and a maintainer of the dataset reviews.

## Correct a row

1. Open the CSV under `datasets/<dataset>/data/` on GitHub and click the
   pencil icon. GitHub makes a copy (fork) for you.
2. Change the row. Keep the commas and quotes as they are.
3. Add a line at the top of `portal.changelog` in the dataset's
   `datapackage.json`, dated today, saying what changed.
4. Propose the change and describe your source in the pull request.

If you would rather not edit, open a
[correction issue](https://github.com/Uganda-Open-Data/datasets/issues/new?template=correction.yml).

## Add a dataset

1. Open a [new dataset issue](https://github.com/Uganda-Open-Data/datasets/issues/new?template=new-dataset.yml)
   first, so we can agree on the source, the licence and the columns.
2. Add a folder named after the dataset's slug (lowercase, words joined by
   hyphens, never renamed once released):

   ```
   datasets/<slug>/
   ├── datapackage.json   title, description, licence, sources, columns, portal block
   ├── README.md          what the data is, notes and known issues, in plain words
   ├── data/*.csv         UTF-8, comma separated, header row
   ├── sources/           optional: a copy of the original document
   └── scripts/           optional: how the CSV was made from the source
   ```

3. Use `datasets/registration-plates/datapackage.json` as the example.
   The `portal` block holds `theme`, `keywords`, `notes`, `knownIssues`,
   `changelog` (newest first) and `key`: the columns that together identify
   a row.

## Rules

- **Public sources only.** Every dataset names its source with a link and
  the date it was published or read.
- **Licences:** CC0-1.0, PDDL-1.0, CC-BY-4.0 and ODC-BY-1.0 are accepted.
  ODbL-1.0 and CC-BY-SA-4.0 (share-alike) need a maintainer's approval,
  recorded as `portal.licenceApprovedBy`. Nothing else is accepted.
- **No personal data.** Public bodies and places only: no names of private
  people, phone numbers, national ID numbers or personal email addresses.
  The checks refuse them.
- **Sign off your commits** (`git commit -s`) to confirm you may share the
  change under the dataset's licence
  ([Developer Certificate of Origin](https://developercertificate.org/)).

## Run the checks yourself

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/check.py      # every dataset
.venv/bin/pytest tools -q            # the checks' own tests
```

## Reviewing (maintainers)

- The source supports the change, and its licence allows sharing.
- The job summary of the `validate` check lists the rows added, changed and
  removed; they match what the pull request says.
- The changelog entry is clear to someone who uses the data.

## Releasing (maintainers)

Tag `main` with today's date and push the tag; the release workflow builds
the tarball and checksums:

```bash
git switch main && git pull
git tag 2026.11.18 && git push origin 2026.11.18
```

Use `2026.11.18.2` for a second release on the same day.
