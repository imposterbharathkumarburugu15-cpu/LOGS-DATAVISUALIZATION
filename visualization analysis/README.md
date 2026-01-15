CSV Data Analysis Project
Description

This project is a simple data analysis tool built using Python.
It works with any CSV file that contains numeric data.

The user can load a CSV file, choose a numeric column, and the program will analyze the data and generate visual outputs.

Technologies Used

1.Python
2.NumPy
3.Pandas
4.Matplotlib

How It Works

User runs the program

User selects a sample CSV or provides their own CSV file

Program displays available numeric columns

User selects one column

Data is cleaned and analyzed

Graphs are generated and saved

Project Structure
visualization analysis/
├── main.py
├── loader.py
├── selector.py
├── processing.py
├── analysis.py
├── visualization.py
├── data/
│   └── sample_any.csv
├── outputs/
│   ├── processed_data.csv
│   └── plots/
│       ├── trend.png
│       └── distribution.png
└── README.md

How to Run
python main.py


Follow the instructions shown in the terminal.

Output

Cleaned CSV file

Trend graph

Distribution graph

All outputs are saved in the outputs folder.

Conclusion

This project shows how Python can be used to analyze CSV data using NumPy, Pandas, and Matplotlib in a simple and practical way.