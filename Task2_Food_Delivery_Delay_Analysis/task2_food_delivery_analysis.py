import pandas as pd
import matplotlib.pyplot as plt


# LOAD DATASET

data = pd.read_csv("food_delivery_delays.csv", encoding="latin1")

print("\n--- Dataset Loaded Successfully ---")
print(data.head())

print("\nDataset Information:")
print(data.info())