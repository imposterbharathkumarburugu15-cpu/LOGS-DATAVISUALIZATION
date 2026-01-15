import matplotlib.pyplot as plt
import os

PLOT_DIR = os.path.join("outputs", "plots")
os.makedirs(PLOT_DIR, exist_ok=True)


def plot_log_levels(freq):
    if not freq:
        print("No log frequency data to plot.")
        return

    plt.figure(figsize=(6, 4))
    plt.bar(freq.keys(), freq.values())
    plt.title("Log Level Distribution")
    plt.xlabel("Log Level")
    plt.ylabel("Count")

    path = os.path.join(PLOT_DIR, "log_levels.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()


def plot_error_trend(trend):
    if trend.empty:
        print("No error trend data to plot.")
        return

    plt.figure(figsize=(8, 4))
    trend.plot()
    plt.title("Error Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Error Count")

    path = os.path.join(PLOT_DIR, "error_trend.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

    
def plot_error_anomalies(trend, anomalies):
    if anomalies.empty:
        print("No anomalies detected.")
        return

    plt.figure(figsize=(8, 4))
    trend.plot(label="Error Count")
    anomalies.plot(style="ro", label="Anomalies")

    plt.title("Error Trend with Anomalies")
    plt.xlabel("Date")
    plt.ylabel("Error Count")
    plt.legend()

    path = os.path.join(PLOT_DIR, "error_anomalies.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

