import pandas as pd
import numpy as np

# Simulate daily electricity data for 1 year
date_range = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')

np.random.seed(42)
data = {
    "Date": date_range,
    "Temperature": np.random.normal(loc=30, scale=5, size=len(date_range)),
    "Humidity": np.random.normal(loc=60, scale=10, size=len(date_range)),
    "WindSpeed": np.random.normal(loc=10, scale=3, size=len(date_range)),
    "Electricity_Consumption": np.random.normal(loc=400, scale=50, size=len(date_range))
}

df = pd.DataFrame(data)

# Add weekend boost (people stay home)
df.loc[df["Date"].dt.weekday >= 5, "Electricity_Consumption"] += 40

# Save CSV
df.to_csv("electricity_data.csv", index=False)
print("✅ Dataset generated and saved as 'electricity_data.csv'")
print(df.head())
