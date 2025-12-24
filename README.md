# Simple ETL Pipeline

## 📌 Project Description
This project is a **simple ETL (Extract, Transform, Load) pipeline** implemented using Python and pandas.
It reads data from a CSV file, applies transformations based on a configuration file, filters records, and writes the transformed data to a new CSV file.

The pipeline is configuration-driven, meaning transformation rules are defined in a JSON file.

---

## 🎯 Purpose of the Project
This project is:
- ✅ A learning exercise
- ✅ A basic ETL implementation
- ❌ Not a production-grade ETL system

It demonstrates how configuration files can control data transformations.

---

## 🛠 Tech Stack
- **Language:** Python
- **Library:** pandas
- **Configuration Format:** JSON
- **Input Format:** CSV
- **Output Format:** CSV

---

## 🏗 How the Code Works
1. Reads transformation rules from `config.json`
2. Loads input data from `input.csv`
3. Keeps only selected columns
4. Renames columns as defined in the configuration
5. Filters rows based on a numeric condition
6. Writes the transformed data to `output.csv`

---

## 📂 Project Files
project/
│

├── etl.py # ETL script

├── config.json # Transformation configuration

├── input.csv # Input data file

├── output.csv # Generated output file

├── README.md # Project documentation

---

## ⚙️ Configuration File (config.json)
The configuration file controls all transformations:

- `columns_to_keep` → Columns to retain
- `rename_columns` → Column renaming rules
- `filter_column` → Column used for filtering
- `filter_value` → Minimum value for filtering

---

## ▶️ How to Run
Run the ETL script using Python:
- python etl.py

📊 Output

After execution:

- A new file named output.csv is created

- Only rows matching the filter condition are included

- Column names are updated as per configuration

The script prints:

ETL completed. Output saved as output.csv

⚠️ Limitations

- Input and output file names are fixed

- Configuration structure must match expected keys

- No command-line arguments

- No automated tests
  
📌 Conclusion

This project demonstrates a basic, configuration-driven ETL pipeline using Python.

It is suitable for learning data transformation concepts and pandas operations.



