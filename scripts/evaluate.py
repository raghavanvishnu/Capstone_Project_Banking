import argparse
from pathlib import Path
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from capstone.model import load_model

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--test", required=True)
    ap.add_argument("--target", default="target")
    args = ap.parse_args()

    model = load_model(args.model)
    df = pd.read_parquet(args.test)
    y_true = df[args.target]
    X = df.drop(columns=[args.target])

    y_prob = model.predict_proba(X)[:, 1]
    y_pred = (y_prob >= 0.5).astype(int)

    auc = roc_auc_score(y_true, y_prob)
    print(f"ROC AUC: {auc:.4f}")
    print(classification_report(y_true, y_pred, digits=4))
