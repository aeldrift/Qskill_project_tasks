import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load dataset
data = pd.read_csv("data/Housing.csv")

# Step 2: Select input features (numbers only)
X = data[
    [
        "area",
        "bedrooms",
        "bathrooms",
        "stories",
        "parking"
    ]
]

# Step 3: Select target variable
y = data["price"]

# Step 4: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Create Linear Regression model
model = LinearRegression()

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Make predictions
predictions = model.predict(X_test)

# Step 8: Evaluate model
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("\nModel Performance:")
print("MAE :", mae)
print("RMSE:", rmse)
print("R²  :", r2)
