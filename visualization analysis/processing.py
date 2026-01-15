import numpy as np

def compute_log_frequencies(df):
    levels = df["level"].values
    unique, counts = np.unique(levels, return_counts=True)
    return dict(zip(unique, counts))