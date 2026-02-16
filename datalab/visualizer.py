import matplotlib.pyplot as plt
import pandas as pd


def plot_column(df: pd.DataFrame, column: str) -> None:
    """
    Plot a histogram of a numeric column.
    """
    if column not in df.columns:
        print("❌ Column not found.")
        return

    plt.hist(df[column])
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

