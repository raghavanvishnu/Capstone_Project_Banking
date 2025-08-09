from __future__ import annotations
import pandas as pd
from pathlib import Path

def read_csv(path: str | Path) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Missing input file: {p}")
    return pd.read_csv(p)

def train_test_split_stratified(df: pd.DataFrame, target: str, test_size: float = 0.2, random_state: int = 42):
    from sklearn.model_selection import train_test_split
    y = df[target]
    X = df.drop(columns=[target])
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
