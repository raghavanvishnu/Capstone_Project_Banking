import argparse
from pathlib import Path
import pandas as pd
from capstone.features import basic_clean, build_features

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--train_out", required=True)
    ap.add_argument("--test_out", required=True)
    ap.add_argument("--target", default="target")
    args = ap.parse_args()

    df = pd.read_csv(args.input)
    df = basic_clean(df)
    df = build_features(df)

    # Simple split
    from sklearn.model_selection import train_test_split

    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=42, stratify=df[args.target]
    )

    Path(args.train_out).parent.mkdir(parents=True, exist_ok=True)
    train_df.to_parquet(args.train_out, index=False)
    test_df.to_parquet(args.test_out, index=False)
    print(f"Saved train -> {args.train_out}, test -> {args.test_out}")
