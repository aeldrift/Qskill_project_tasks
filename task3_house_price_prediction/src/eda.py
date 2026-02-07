# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt


# Step 2: Load the dataset
data = pd.read_csv("data/Housing.csv")


# Step 3: See first 5 rows
print("First 5 rows:")
print(data.head())


# Step 4: Check number of rows and columns
print("\nShape of dataset:")
print(data.shape)


# Step 5: Check column names
print("\nColumn names:")
print(data.columns)


# Step 6: Check basic statistics
print("\nBasic statistics:")
print(data.describe())


# Step 7: Plot house price distribution
plt.hist(data["price"], bins=30)
plt.xlabel("House Price")
plt.ylabel("Count")
plt.title("House Price Distribution")
plt.show()
