# data exploration / EDAs

# Imports
import pandas as pd
import os
import json

# Read data
file_names = os.listdir("data")

ev = pd.read_csv(
    os.path.join("data", file_names[0]), index_col=0
)  # this is historical data
chargers = pd.read_csv(os.path.join("data", file_names[1]), index_col=0)
energy_prod = pd.read_csv(os.path.join("data", file_names[2]), index_col=0)


# Understanding variables
def export_unique_values_json(data, filename):
    unique_values = {
        col: data[col].astype(int).unique().tolist()
        if data[col].dtype == "int64"
        else list(data[col].unique())
        for col in data.columns
    }

    filepath = os.path.join("data", f"{filename}.json")

    with open(filepath, "w") as f:
        json.dump(unique_values, f, indent=4)

    return print("File saved successfully!")


## Run the following only once, then lookup unique values
## export_unique_values_json(ev, "ev_unique_values")
## export_unique_values_json(chargers, "chargers_unique_values")
## export_unique_values_json(energy_prod, "energy_prod_unique_values")

# Actual exploration
