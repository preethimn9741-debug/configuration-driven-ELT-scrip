import pandas as pd
import json

with open("config.json") as f:
    config = json.load(f)

df = pd.read_csv("input.csv")

df = df[config["columns_to_keep"]]

df = df.rename(columns=config["rename_columns"])


col = config["filter_column"]
value = config["filter_value"]
df = df[df[col] > value]

df.to_csv("output.csv", index=False)

print("ETL completed. Output saved as output.csv")
