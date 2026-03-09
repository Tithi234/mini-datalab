import pandas as pd

def clean_missing(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.dropna()
    return cleaned_df

