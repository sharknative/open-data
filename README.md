# Sharknative open data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23645940.svg)](https://doi.org/10.5281/zenodo.23645940)

Sharknative publishes product-research sites; these are the open data tables behind their tools. Each table holds maker-published specs with a source URL per cell. Cells with no published figure are left blank. The canonical, latest copy of every table lives on its page; this repo mirrors those files for people who prefer git, CSV or JSON.

## Datasets

| Folder | Table | Rows | Page |
|---|---|---|---|
| `countertopcheck-fit/` | Countertop appliance heights and cabinet clearances | 59 | https://countertopcheck.com/fit/ |
| `anglerleague-castable-sonar-index/` | Castable Sonar Spec Index | 11 | https://anglerleague.com/castable-sonar-index/ |
| `cremacheck-office-machines/` | Office espresso machine data | 12 | https://cremacheck.com/office/ |
| `firstprintcheck-first-printers/` | First-printer data | 10 | https://firstprintcheck.com/tools/first-printer-picker/ |
| `wellnessrundown-small-space-index/` | Small-Space Fitness Index | 29 | https://wellnessrundown.com/small-space-index/ |

Coming: VettedFur automatic litter box specs (https://vettedfur.com/data/automatic-litter-boxes/) once that page publishes a CSV.

Each folder has the CSV, the JSON and a README with the source page, the gathering method, a citation line and, where the site offers one, an iframe embed snippet.

## Cite

Sharknative (2026). *Sharknative open data: maker-published spec tables* (v2026.10.25) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23645940

## License

CC BY 4.0 (see `LICENSE`). Credit the brand named in the dataset README and link to its page.

## How to refresh

`py -3.11 refresh.py` re-downloads every CSV and JSON in the `DATASETS` list from its live URL, writes the files in place and prints which files changed. It does not commit. A weekly scheduled run on Sharknative's side does the same and pushes.

Last checked: 2026-10-24
