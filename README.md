# Fraud Detection Capstone

Goal: build a reproducible pipeline to detect fraudulent transactions and report model performance.

## Dataset
Due to size, the dataset is stored externally:  
**📂 Google Drive:** https://drive.google.com/drive/u/0/folders/1F7Du5Ey0ab9xprD0w_f8-yAbXt_sB8OP  
*Access:* view-only. Download `dataset.csv` to `data/raw/`.

**Target column:** `<to-fill>`  
**Positive class (fraud = 1?):** `<to-fill>`

## Quickstart
```bash
make setup
make eda      # run EDA notebook (parameterized)
make train    # train baseline model
make eval     # evaluate and print metrics
```

## Structure
- `notebooks/` — Jupyter notebooks (`01_eda.ipynb`, `02_model.ipynb`)
- `src/capstone/` — importable Python package with pipeline modules
- `data/raw|interim|processed` — keep PII out of Git
- `models/` — serialized models (ignored by Git)
- `reports/` — figures and generated reports
- `scripts/` — small CLI entrypoints
- `tests/` — pytest unit tests
- `.github/workflows/ci.yml` — CI that runs lint + tests

## Reproducibility
- Python 3.11
- `requirements.txt`
- `Makefile` targets are the source of truth

## Secrets
- Use a local `.env` (not committed). CI secrets via GitHub → Settings → Secrets and variables → Actions.
