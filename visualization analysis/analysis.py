import numpy as np
import pandas as pd
def error_trend(df):
    error_df = df[df["level"] == "ERROR"]
    trend = error_df.groupby(
        error_df["timestamp"].dt.date
    ).size()
    return trend


def detect_error_anomalies(trend, z_threshold=3):

    values = trend.values.astype(float)

    mean = np.mean(values)
    std = np.std(values)

    if std == 0:
        return trend, pd.Series(dtype=float)

    z_scores = (values - mean) / std
    anomaly_mask = np.abs(z_scores) > z_threshold

    anomalies = trend[anomaly_mask]

    return trend, anomalies
