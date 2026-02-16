import pandas as pd


def show_summary(df: pd.DataFrame) -> None:
    """
    Display basic summary statistics.
    """
    print("\n📊 Data Summary:")
    print(df.describe())

