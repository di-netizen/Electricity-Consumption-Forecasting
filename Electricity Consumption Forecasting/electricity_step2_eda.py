import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("electricity_data.csv")

# Convert date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Feature engineering
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.weekday
df['Day'] = df['Date'].dt.day

# Plot electricity consumption trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Electricity_Consumption')
plt.title("📉 Electricity Consumption Over Time")
plt.xlabel("Date")
plt.ylabel("Electricity (kWh)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot: Monthly distribution
plt.figure(figsize=(10, 5))
sns.boxplot(x='Month', y='Electricity_Consumption', data=df)
plt.title("📦 Monthly Electricity Consumption Distribution")
plt.tight_layout()
plt.show()
