def select_numeric_column(df):
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if not numeric_cols:
        raise ValueError("No numeric columns found in this CSV.")

    print("\nAvailable numeric columns:")
    for i, col in enumerate(numeric_cols, start=1):
        print(f"{i}. {col}")

    choice = input("Select a column number for analysis: ").strip()

    if not choice.isdigit() or int(choice) not in range(1, len(numeric_cols)+1):
        raise ValueError("Invalid column selection.")

    return numeric_cols[int(choice)-1]