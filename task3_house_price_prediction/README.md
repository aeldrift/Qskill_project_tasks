🏠 **House Price Prediction using Machine Learning & Streamlit**

🎯 **Problem Statement**

Accurately estimating house prices is a common real-world challenge in the real estate industry. Property prices depend on multiple factors such as area, number of bedrooms, bathrooms, stories, and parking availability.


**TASK:** Develop a linear regression model to predict house price based on features such as the number of rooms, location, size and other relevant factors. Collect a suitable dataset from Kaggle, preprocess it, and train the model to make accurate predictions.

📖 **Project Overview**

This project implements an end-to-end House Price Prediction system using a Linear Regression model.

The dataset is explored and analyzed to understand price patterns, after which a machine learning model is trained to predict house prices based on user-provided inputs. A Streamlit web app is built on top of the model to allow users to interactively input house details and instantly view predictions along with statistical insights and visualizations.

I analyzed housing data, trained a regression model, and built an interactive web app to predict house prices and visualize pricing trends.

📂 **Dataset Description**

Dataset Name: Housing.csv

Source: Kaggle (Open-source dataset for educational purposes)

🔗 **Dataset Link:**
https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction

Dataset Columns

price – Price of the house

area – Total area of the house (in sq ft)

bedrooms – Number of bedrooms

bathrooms – Number of bathrooms

stories – Number of floors

parking – Number of parking spaces

(Additional categorical features are present but not used in this model)

🛠️ **Tools & Technologies Used**

• Python

• Pandas – Data loading and analysis

• Scikit-learn – Machine Learning (Linear Regression)

• Streamlit – Interactive web application

• Plotly – Interactive data visualization

• Matplotlib – Exploratory analysis (optional)

📊 **Features of the Application**

✅ User-friendly sidebar inputs
✅ Instant house price prediction
✅ Dataset statistics displayed after prediction
✅ Interactive price distribution graph with hover values
✅ Clean and modern UI
✅ Beginner-friendly and well-structured code

🖥️ **Application Workflow**

User enters house details (area, bedrooms, bathrooms, stories, parking)

Clicks Predict Price


**The app displays:**

Predicted house price

Dataset statistics

Interactive house price distribution chart

All outputs are shown only after clicking the Predict button to improve user experience.

📈 **Insights & Observations**

• House price increases with larger area and more rooms

• There is a strong relationship between house size and price

• Interactive visualizations help understand overall price distribution

• The model provides reasonable baseline predictions using linear regression

📁 **Project Structure**
```
House_Price_Prediction/
│
├── app.py                # Streamlit application
├── data/
│   └── Housing.csv       # Dataset
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
```

⚙️ **Requirements**

Python 3.8 or higher

Required Python Libraries

• pandas

• scikit-learn

• streamlit

• plotly

• matplotlib

**Install Dependencies**
```pip install pandas scikit-learn streamlit plotly matplotlib```

▶️ **How to Run the Project ?**

1️⃣ **Navigate to the project directory**

```cd House_Price_Prediction```

2️⃣ **Run the Streamlit app**

```streamlit run app.py```


**Open the browser at:**

```http://localhost:8501```

🎓 **Learning Outcomes**

Through this project, I learned:

• How to preprocess and analyze real-world datasets

• How to train and use a regression model

• How to integrate machine learning with a web interface

• How to create interactive visualizations

• How to structure and document an ML project professionally

🚀 **Future Improvements**

• Add feature scaling and categorical encoding

• Train advanced models (Random Forest, XGBoost)

• Evaluate model performance using metrics (R², RMSE)

• Deploy the app on Streamlit Cloud