import pandas as pd


def clean_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows with missing values.
    """
    cleaned_df = df.dropna()
    print("🧹 Missing values removed.")
    return cleaned_df

