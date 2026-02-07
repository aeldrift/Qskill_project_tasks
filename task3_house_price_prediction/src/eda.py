import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/Housing.csv")

st.subheader("🔍 Exploratory Data Analysis (EDA)")

# Show first 5 rows
st.write("### First 5 Rows of Dataset")
st.dataframe(data.head())

# Show shape
st.write("### Dataset Shape")
st.write(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")

# Show column names
st.write("### Column Names")
st.write(list(data.columns))

# Show basic statistics
st.write("### Basic Statistics")
st.dataframe(data.describe())

# Plot house price distribution
st.write("### 📈 House Price Distribution")

plt.figure(figsize=(8, 4))
plt.hist(data["price"], bins=30)
plt.xlabel("House Price")
plt.ylabel("Count")
plt.title("House Price Distribution")

st.pyplot(plt)
