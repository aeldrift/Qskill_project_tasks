🎯 **Problem Statement**
Food delivery platforms often face delays due to multiple factors such as traffic congestion, distance, and weather conditions.

**TASK**: Using the Pandas library, load a CSV file and perform basic data analysis tasks, such as
calculating the average of a selected column. Additionally, use Matplotlib to create
visualizations, including bar charts, scatter plots, and heatmaps, to analyze the data. Provide
insights and observations based on the analysis and visualizations.

**Each visualization is displayed separately to focus on individual insights.**

📖 **Project Overview**

This project analyzes food delivery data to understand the key factors that contribute to delivery delays. Using Python’s Pandas and Matplotlib libraries, the dataset is explored through statistical analysis and visualizations to uncover patterns related to distance, traffic conditions, and overall delivery time.

The goal of this study is to identify which factors most strongly influence delivery delays and to extract practical, operational insights from real-world data.

(I analyzed real food delivery data to identify how traffic and conditions affect delivery delays. Tried to get cleaned the data, visualized trends, and created delay categories to extract operational insights.)

📂 **Dataset Description**

**Data Source:** The dataset used in this project is an open-source food delivery dataset obtained from **Kaggle** for educational and analytical purposes.

🔗Link to dataset: https://www.kaggle.com/datasets/willianoliveiragibin/food-delivery-time

The dataset (food_delivery_delays.csv) represents real-world food delivery orders and contains the following columns:

**• Order_ID –**  Unique identifier for each delivery order
**• Distance_km –**  Distance between the restaurant and the customer
**• Traffic_Level –** Traffic condition during delivery (Low, Medium, High)
**• Weather – Weather –** condition at the time of delivery
**• Delivery_Time_min –**  Total delivery time in minutes 


🛠️ **Tools & Libraries Used**

**• Python**

**• Pandas –**  Data loading, cleaning, and analysis

**• Matplotlib –**  Data visualization



📊 **Data Analysis & Visualizations**

**1️.  Average Delivery Time**

The average delivery time is calculated using Pandas to understand the overall delivery performance.

**2️.  Bar Chart – Traffic Level vs Delivery Time**

This visualization shows how delivery time increases as traffic congestion changes from Low to High.

**3️. Scatter Plot – Distance vs Delivery Time**

The scatter plot visualizes the relationship between delivery distance and delivery time.

**4️. Heatmap – Correlation Analysis**

A heatmap is used to identify correlations between numerical variables, highlighting strong relationships that impact delivery delays.


🔍 **Insights & Observations**

The average delivery time is approximately 35–40 minutes, indicating moderate delivery delays.

Delivery time increases significantly as traffic conditions shift from Low to High, making traffic congestion a major contributing factor.

The scatter plot shows a positive relationship between distance and delivery time, meaning longer distances generally result in longer delivery times.

The heatmap confirms a strong correlation between distance and delivery time.

Overall, traffic conditions appear to have a greater impact on delivery delays than distance alone.


📁 **Project Structure**
```
Task2_Food_Delivery_Delay_Analysis/
│
├── food_delivery_delays.csv
├── task2_food_delivery_analysis.py
└── README.md 
```

⚙️ **Requirements**

Python 3.8 or higher

**Required Python libraries:**

• pandas

• numpy

• matplotlib

• seaborn

• streamlit (optional)

**Install dependencies:**


``` pip install pandas numpy matplotlib seaborn streamlit ```


▶️ How to Run the Project

1️⃣ Navigate to the project directory

``` cd Task2_Food_Delivery_Delay_Analysis ```

2️⃣ Run the analysis script

``` python task2_food_delivery_analysis.py ```

This will:

- Load the dataset

- Perform delivery delay analysis

- Output results (prints/plots depending on implementation)

📊 **Streamlit UI** (Optional)

If you want to explore the analysis using an interactive web interface:

``` streamlit run delivery_ui_app.py  ```

After running the command, open the local URL shown in the terminal (usually http://localhost:8501) in your browser.