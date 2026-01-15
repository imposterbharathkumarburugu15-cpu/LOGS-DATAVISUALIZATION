import pandas as pd
REQUIRED_COLUMNS={"timestamp","level","message"}
def load_user_data(path):
    try:
        path = path.strip().strip('"').strip("'")
        df = pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Error loading CSV file: {e}")
    if not REQUIRED_COLUMNS.issubset(df.columns):
        raise ValueError(f"CSV file must contain the following columns: {REQUIRED_COLUMNS}")
    df["timestamp"]=pd.to_datetime(df["timestamp"],errors="coerce")
    df=df.dropna(subset=["timestamp"])
    return df