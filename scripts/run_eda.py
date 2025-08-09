import argparse
from pathlib import Path
import pandas as pd

def summarize(df: pd.DataFrame) -> str:
    lines = []
    lines.append(f"Rows: {len(df):,}  Cols: {df.shape[1]}")
    lines.append("\nColumns:")
    lines.extend([f"- {c} ({df[c].dtype})  missing={df[c].isna().sum()}" for c in df.columns])
    lines.append("\nClass balance (if 'target' exists):")
    if 'target' in df.columns:
        lines.append(str(df['target'].value_counts(normalize=True)))
    return "\n".join(lines)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    df = pd.read_csv(args.input)
    out = summarize(df)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(out, encoding="utf-8")
    print(out)
