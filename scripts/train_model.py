import argparse
from pathlib import Path
import pandas as pd
from capstone.model import make_baseline_pipeline, save_model

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="processed train parquet")
    ap.add_argument("--model", required=True, help="output model path")
    ap.add_argument("--target", default="target")
    args = ap.parse_args()

    df = pd.read_parquet(args.input)
    y = df[args.target]
    X = df.drop(columns=[args.target])

    cat_cols = [c for c in X.columns if X[c].dtype == "object"]
    num_cols = [c for c in X.columns if c not in cat_cols]

    pipe = make_baseline_pipeline(cat_cols, num_cols)
    pipe.fit(X, y)

    Path(args.model).parent.mkdir(parents=True, exist_ok=True)
    save_model(pipe, args.model)
    print(f"Saved model -> {args.model}")
