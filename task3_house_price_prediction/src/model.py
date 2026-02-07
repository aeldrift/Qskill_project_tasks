import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


def train_model():
    """
    This function:
    1. Loads the dataset
    2. Selects important features
    3. Scales the features
    4. Trains a Linear Regression model
    5. Returns the trained model and scaler
    """

    # STEP 1: Load the dataset from CSV file
    data = pd.read_csv("data/Housing.csv")

    # STEP 2: Select input features (X)
    # These are the values the model will learn from
    X = data[[
        "area",
        "bedrooms",
        "bathrooms",
        "stories",
        "parking"
    ]]

    # STEP 3: Select target variable (y)
    # This is the value we want to predict
    y = data["price"]

    # STEP 4: Scale the input features
    # Scaling helps the model understand all features equally
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # STEP 5: Create and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_scaled, y)

    # STEP 6: Return the trained model and scaler
    return model, scaler
