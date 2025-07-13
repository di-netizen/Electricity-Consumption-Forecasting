import pandas as pd
import joblib

# Load model
model = joblib.load("electricity_model.pkl")

# Example new input (forecasting next day's usage)
new_data = pd.DataFrame([{
    'Temperature': 32,
    'Humidity': 58,
    'WindSpeed': 12,
    'Month': 7,
    'Weekday': 3  # Thursday
}])

# Predict
prediction = model.predict(new_data)[0]
print(f"🔮 Predicted Electricity Consumption: {round(prediction, 2)} kWh")

