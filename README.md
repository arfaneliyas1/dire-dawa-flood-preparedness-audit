# Dire Dawa Flood Preparedness Audit

This repository contains the public research materials for **From Flood Maps to Action: An Open-Data Audit of Flood Preparedness and Early-Warning Evidence in Dire Dawa, Ethiopia**. The immutable `v1.0` package and DOI should be archived through Zenodo.

## Contents

- `report/`: technical report and four-page executive brief.
- `data/`: source inventory, finding-level evidence matrix, quality scorecard, and data dictionary.
- `analysis/`: notebook and scripts describing cleaning and figure-generation logic.
- `methodology/`: protocol, source-selection log, scoring rubric, and ethical/data-protection note.
- `outputs/`: derived figures and summary tables.

## Evidence boundary

This is a secondary-evidence audit. It does not claim current operational readiness, service absence, or citywide coverage where current location-specific evidence is unavailable. Historical program evidence, technical models, plans, household studies, and operational records are treated as different evidence types.

## Reproducibility

The core inputs are the CSV files in `data/`. The figures in `outputs/figures/` are derived from the evidence matrix and scorecard. The notebook and Python scripts document the cleaning and figure-generation workflow.

## Licensing and third-party material

Original report text, original charts, methods, derived tables, and original data compilations in this package are released under CC BY 4.0. External sources are cited and linked in the source inventory. Restricted microdata, copyrighted PDFs, and third-party maps or datasets are not redistributed here.

## Public-release exclusions

This repository intentionally excludes restricted microdata, copyrighted source PDFs, sensitive maps, vulnerable-household data, unverified evacuation or facility locations, temporary files, personal credentials, and duplicate ZIP archives.

## Citation

See `CITATION.cff` for citation metadata. Repository release: public preparation for the Zenodo `v1.0` archive. Publication date: 2026-10-06.
