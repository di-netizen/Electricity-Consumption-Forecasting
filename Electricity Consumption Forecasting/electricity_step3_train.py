import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load data
df = pd.read_csv("electricity_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Feature engineering
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.weekday

# Features and target
X = df[['Temperature', 'Humidity', 'WindSpeed', 'Month', 'Weekday']]
y = df['Electricity_Consumption']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict & Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model Trained")
print("📉 Mean Squared Error:", round(mse, 2))
print("📊 R² Score:", round(r2, 2))

# Save model
joblib.dump(model, "electricity_model.pkl")
print("💾 Model saved as 'electricity_model.pkl'")
