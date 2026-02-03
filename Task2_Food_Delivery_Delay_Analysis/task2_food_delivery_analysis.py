import pandas as pd
import matplotlib.pyplot as plt


# LOAD DATASET

data = pd.read_csv("food_delivery_delays.csv", encoding="latin1")

print("\n--- Dataset Loaded Successfully ---")
print(data.head())

print("\nDataset Information:")
print(data.info())

# SELECTING RELEVANT COLUMNS

columns_used = [
    "Delivery_time(min)",
    "Road_traffic_density",
    "Weather_conditions"
]

data = data[columns_used]

print("\nSelected Columns Preview:")
print(data.head())


# DATA CLEANING

data = data.dropna()

print("\nAfter Removing Missing Values:")