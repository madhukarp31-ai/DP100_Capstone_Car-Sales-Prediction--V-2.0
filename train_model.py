import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import os

# Load the cleaned dataset (make sure this is the path used in Day 2)
df = pd.read_csv("cleaned_car_sales.csv")

# Optional: Verify for remaining non-numeric columns
print("Columns and types:\n", df.dtypes)

# Drop non-numeric columns if any still exist (safety)
df = df.select_dtypes(include=["float64", "int64"])

# Define features and label
X = df.drop("Price", axis=1)
y = df["Price"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5

print(f"RMSE: {rmse}")

# Save model
os.makedirs("outputs", exist_ok=True)
joblib.dump(model, "outputs/model.joblib")
