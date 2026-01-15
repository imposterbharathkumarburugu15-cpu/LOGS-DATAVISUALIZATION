import numpy as np
import pandas as pd

def basic_statistics(arr):
    return {
        "mean": np.mean(arr),
        "std": np.std(arr),
        "min": np.min(arr),
        "max": np.max(arr)
    }

def detect_anomalies(arr, z_threshold=3):
    mean = np.mean(arr)
    std = np.std(arr)

    if std == 0:
        return pd.Series(dtype=float)

    z_scores = (arr - mean) / std
    anomalies = arr[abs(z_scores) > z_threshold]

    return anomalies