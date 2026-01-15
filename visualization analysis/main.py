from loader import load_user_data
from processing import compute_log_frequencies
from analysis import error_trend
from visualization import plot_log_levels, plot_error_trend
from analysis import error_trend, detect_error_anomalies
from visualization import plot_error_anomalies

import os

def main():
    print("Choose data source:")
    print("1. Use sample log file")
    print("2. Provide your own CSV file path")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        path = "data/sample_logs.csv"
        print("Using sample log file.")
    elif choice == "2":
        path = input("Enter path to your CSV file: ").strip()
    else:
        print("Invalid choice. Exiting.")
        return

    try:
        df = load_user_data(path)
    except ValueError as e:
        print(e)
        return

    print("Data loaded successfully:", df.shape)


    freq = compute_log_frequencies(df)
    trend = error_trend(df)

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/processed_logs.csv", index=False)

    plot_log_levels(freq)
    plot_error_trend(trend)
    print("Sample rows:")
    print(df.head())
    trend = error_trend(df)
    trend, anomalies = detect_error_anomalies(trend)

    plot_error_anomalies(trend, anomalies)

    print("\nAnalysis complete.")
    print("Processed data saved to outputs/processed_logs.csv")
    print("Plots saved in outputs/plots/")

if __name__ == "__main__":
 main()
