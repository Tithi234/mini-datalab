import matplotlib.pyplot as plt
import pandas as pd

def plot_column(df: pd.DataFrame, column: str):

    fig, ax = plt.subplots()

    ax.hist(df[column])
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    return fig
