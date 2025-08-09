# Runbook

## End-to-End
1. Place source CSV at `data/raw/dataset.csv` (do not commit).
2. `make setup`
3. `make eda` → writes `reports/eda_summary.txt` and figures.
4. Preprocess data (see `scripts/preprocess.py`) to create parquet files.
5. `make train` → trains and saves `models/model.pkl`.
6. `make eval` → prints metrics and saves a confusion matrix to `reports/`.
