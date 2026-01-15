import pandas as pd

def load_csv_any_format(path):
    try:
        path = path.strip().strip('"').strip("'")
        df = pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Error loading CSV file: {e}")

    if df.empty:
        raise ValueError("CSV file is empty.")

    return df