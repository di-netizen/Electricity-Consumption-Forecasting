import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import joblib

# Load data and model
df = pd.read_csv("electricity_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.weekday

X = df[['Temperature', 'Humidity', 'WindSpeed', 'Month', 'Weekday']]
y = df['Electricity_Consumption']

model = joblib.load("electricity_model.pkl")
y_pred = model.predict(X)

# Plot actual vs predicted
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], y, label='Actual', color='blue')
plt.plot(df['Date'], y_pred, label='Predicted', color='orange', alpha=0.7)
plt.title("⚡ Electricity Consumption: Actual vs Predicted")
plt.xlabel("Date")
plt.ylabel("Consumption (kWh)")
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

