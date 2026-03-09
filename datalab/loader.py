import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print("File loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

