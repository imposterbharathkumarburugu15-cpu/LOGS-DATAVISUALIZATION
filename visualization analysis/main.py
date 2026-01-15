from loader import load_csv_any_format
from selector import select_numeric_column
from processing import clean_numeric_series
from analysis import basic_statistics, detect_anomalies
from visualization import plot_series, plot_distribution

import os
import pandas as pd

def main():
    print("Choose data source:")
    print("1. Use sample CSV")
    print("2. Provide your own CSV file")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        path = "data/sample_any.csv"
    elif choice == "2":
        path = input("Enter CSV file path: ")
    else:
        print("Invalid choice.")
        return

    df = load_csv_any_format(path)

    print("\nCSV Loaded Successfully")
    print("Columns:", list(df.columns))

    column = select_numeric_column(df)

    arr = clean_numeric_series(df[column])

    stats = basic_statistics(arr)
    anomalies = detect_anomalies(arr)

    os.makedirs("outputs", exist_ok=True)
    pd.DataFrame({"value": arr}).to_csv("outputs/processed_data.csv", index=False)

    plot_series(arr, column)
    plot_distribution(arr, column)
 



    print("\nAnalysis Complete")
    print("Statistics:", stats)
    
    print("Anomalies detected:", len(anomalies))
    print("Outputs saved in outputs/ folder")

if __name__ == "__main__":
    main()
