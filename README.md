# Fraud Detection Capstone

Reproducible, production-minded scaffold for a fraud detection project.

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
