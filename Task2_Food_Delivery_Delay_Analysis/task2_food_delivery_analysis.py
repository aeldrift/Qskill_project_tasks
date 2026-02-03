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
print(data.info())



# BASIC DATA ANALYSIS

average_delivery_time = data["Delivery_time(min)"].mean()
print("\nAverage Delivery Time (minutes):", round(average_delivery_time, 2))


# BAR CHART

traffic_delay = data.groupby(
    "Road_traffic_density"
)["Delivery_time(min)"].mean()

plt.figure()    # Average Delivery Time by Traffic Density
traffic_delay.plot(kind="bar")
plt.title("Average Delivery Time by Traffic Density")
plt.xlabel("Traffic Density")
plt.ylabel("Average Delivery Time (minutes)")
plt.show()