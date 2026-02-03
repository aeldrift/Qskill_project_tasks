import os
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # directory where this script is located


csv_path = os.path.join(BASE_DIR, "food_delivery_delays.csv")   # path to CSV file

# Load dataset
data = pd.read_csv(csv_path, encoding="latin1")

print("\n--- Dataset Loaded Successfully ---")
print(data.head())

print("\nDataset Information:")
print(data.info())




# SELECT RELEVANT COLUMNS

columns_used = [
    "Time_taken(min)",
    "Type_of_vehicle",
    "Type_of_order"
]

data = data[columns_used]

print("\nSelected Columns Preview:")
print(data.head())



# DATA CLEANING

data = data.dropna()

print("\nAfter Removing Missing Values:")
print(data.info())


# BASIC DATA ANALYSIS

average_delivery_time = data["Time_taken(min)"].mean()
print("\nAverage Delivery Time (minutes):", round(average_delivery_time, 2))



# BAR CHART
# Average Delivery Time by Vehicle Type

vehicle_delay = data.groupby(
    "Type_of_vehicle"
)["Time_taken(min)"].mean()

plt.figure()
vehicle_delay.plot(kind="bar")
plt.title("Average Delivery Time by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Delivery Time (minutes)")
plt.show()



# SCATTER PLOT
# Delivery Time Distribution

plt.figure()
plt.scatter(range(len(data)), data["Time_taken(min)"])
plt.title("Delivery Time Distribution Across Orders")
plt.xlabel("Order Index")
plt.ylabel("Delivery Time (minutes)")
plt.show()


# HEATMAP

plt.figure()
plt.imshow(data[["Time_taken(min)"]].corr())
plt.colorbar()
plt.title("Correlation Heatmap")
plt.show()


# SMART INSIGHT
# Delay Category

data["Delay_Category"] = data["Time_taken(min)"].apply(
    lambda x: "On Time" if x <= 30 else "Delayed"
)

print("\nDelay Category Count:")
print(data["Delay_Category"].value_counts())


# BAR CHART
# On-Time vs Delayed Deliveries

plt.figure()
data["Delay_Category"].value_counts().plot(kind="bar")
plt.title("On-Time vs Delayed Deliveries")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.show()
