import matplotlib.pyplot as plt
import os

PLOT_DIR = os.path.join("outputs", "plots")
os.makedirs(PLOT_DIR, exist_ok=True)

def plot_series(arr, column_name):
    plt.figure(figsize=(8,4))
    plt.plot(arr)
    plt.title(f"{column_name} Trend")
    plt.xlabel("Index")
    plt.ylabel(column_name)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, "trend.png"), dpi=300)
    plt.close()

def plot_distribution(arr, column_name):
    plt.figure(figsize=(6,4))
    plt.hist(arr, bins=30)
    plt.title(f"{column_name} Distribution")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, "distribution.png"), dpi=300)
    plt.close()
def plot_anomalies(arr, anomalies, column_name):
    plt.figure(figsize=(8,4))
    plt.plot(arr, label="Data")
    if not anomalies.empty:
        plt.scatter(anomalies.index, anomalies.values, color='red', label="Anomalies")
    plt.title(f"{column_name} with Anomalies")
    plt.xlabel("Index")
    plt.ylabel(column_name)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, "anomalies.png"), dpi=300)
    plt.close()