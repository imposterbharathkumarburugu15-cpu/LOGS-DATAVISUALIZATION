import numpy as np

def clean_numeric_series(series):
    arr = series.to_numpy(dtype=float)

    mean = np.nanmean(arr)
    arr = np.where(np.isnan(arr), mean, arr)

    return arr