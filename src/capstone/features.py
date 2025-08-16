import pandas as pd


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    # Example minimal cleaning — customize as needed
    df = df.copy()
    # Strip column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    # Drop exact duplicates
    df = df.drop_duplicates()
    return df


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: add domain-specific features
    return df
