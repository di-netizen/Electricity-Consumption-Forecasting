## Electricity Consumption Forecasting

A robust Python project that simulates daily electricity usage based on weather and calendar data, builds a Random Forest forecasting model, and provides easy scripts for data visualization, training, inference, and evaluation.

---

### 🔍 Features

- **Data Simulation**: Generates one year of synthetic weather and electricity usage records, with a weekend consumption boost.  
- **Exploratory Analysis**: Line and box plots to inspect trends and seasonal patterns.  
- **Model Training**: Splits data, trains a Random Forest regressor, evaluates performance, and persists the model.  
- **Inference**: Simple script to load the model and predict next-day electricity consumption.  
- **Evaluation**: Overlay of actual vs. predicted consumption for comprehensive performance review.  

---

### 🛠️ Prerequisites

- Python 3.7 or above  
- `pandas`  
- `numpy`  
- `scikit-learn`  
- `matplotlib`  
- `seaborn`  
- `joblib`  

Install dependencies via:
```bash
pip install -r requirements.txt
