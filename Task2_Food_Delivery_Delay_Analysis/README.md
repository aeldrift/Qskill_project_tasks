This project analyzes food delivery data to understand the key factors that contribute to delivery delays. Using Python’s Pandas and Matplotlib libraries, the dataset is explored through statistical analysis and visualizations to uncover patterns related to distance, traffic conditions, and overall delivery time.


What Actually Drives Food Delivery Delays?
A Data Analysis and Visualization Study using Python


📂 Dataset Description

The dataset (food_delivery_delays.csv) contains the following columns:
• Order_ID – Unique identifier for each order

• Distance_km – Distance between restaurant and customer

• Traffic_Level – Traffic condition during delivery (Low, Medium, High)

• Weather – Weather condition at the time of delivery

• Delivery_Time_min – Total delivery time in minutes


🛠️ Tools & Libraries Used

• Python

• Pandas – Data loading and analysis

• Matplotlib – Data visualization


📊 Data Analysis & Visualizations

1️.  Average Delivery Time

The average delivery time is calculated using Pandas to understand typical delivery performance.

2️.  Bar Chart – Traffic Level vs Delivery Time

Shows how delivery time increases with traffic congestion.

3️. Scatter Plot – Distance vs Delivery Time

Visualizes the relationship between delivery distance and delivery time.

4️. Heatmap – Correlation Analysis

Displays the correlation between numerical variables to identify strong relationships.

🔍 Insights & Observations

The average delivery time is approximately 35–40 minutes, indicating moderate delivery delays.

Delivery time increases significantly as traffic changes from Low to High, making traffic a major factor.

The scatter plot shows a positive relationship between distance and delivery time—longer distances usually take more time.

The heatmap confirms a strong correlation between distance and delivery time.

External factors such as traffic conditions play a more critical role than distance alone.


📁 Project Structure

Task2_Food_Delivery_Delay_Analysis/
│
├── food_delivery_delays.csv
├── task2_food_delivery_analysis.py
└── README.md
