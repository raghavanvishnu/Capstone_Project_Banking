
        .PHONY: setup fmt lint test eda train eval clean

        PY=python
        PIP=pip

        setup:
		$(PIP) install -U pip
		$(PIP) install -r requirements.txt
		@echo "✅ Environment ready."

        fmt:
		$(PY) -m black src tests scripts

        lint:
		$(PY) -m ruff check src tests scripts

        test:
		$(PY) -m pytest -q

        eda:
		$(PY) scripts/run_eda.py --input data/raw/dataset.csv --out reports/eda_summary.txt

        train:
		$(PY) scripts/train_model.py --input data/processed/train.parquet --model models/model.pkl

        eval:
		$(PY) scripts/evaluate.py --model models/model.pkl --test data/processed/test.parquet

        clean:
		rm -rf __pycache__ .pytest_cache .coverage dist build
