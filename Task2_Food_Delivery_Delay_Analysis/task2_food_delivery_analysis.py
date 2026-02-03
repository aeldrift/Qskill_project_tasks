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


# SCATTER PLOT

plt.figure()    # Delivery Time Distribution
plt.scatter(range(len(data)), data["Delivery_time(min)"])   
plt.title("Delivery Time Distribution Across Orders")
plt.xlabel("Order Index")
plt.ylabel("Delivery Time (minutes)")
plt.show()


#  HEATMAP 

numeric_data = data[["Delivery_time(min)"]]

plt.figure()
plt.imshow(numeric_data.corr())
plt.colorbar()
plt.title("Correlation Heatmap")
plt.show()



# SMART INSIGHT

data["Delay_Category"] = data["Delivery_time(min)"].apply(
    lambda x: "On Time" if x <= 30 else "Delayed"   # Delay Category
)

print("\nDelay Category Count:")
print(data["Delay_Category"].value_counts())



# BAR CHART

plt.figure()
data["Delay_Category"].value_counts().plot(kind="bar")  # On-Time vs Delayed Deliveries
plt.title("On-Time vs Delayed Deliveries")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.show()
