import numpy as np
import joblib
from influxdb_client import InfluxDBClient

# ----------------------------
# InfluxDB Configuration
# ----------------------------
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "pulse-ai-secure-token"
ORG = "pulse-ai"
BUCKET = "metrics"

# ----------------------------
# Load trained models
# ----------------------------
cpu_model = joblib.load("models/cpu_model.pkl")
ram_model = joblib.load("models/ram_model.pkl")

# ----------------------------
# Prediction function
# ----------------------------
def predict_future(steps=10):
    X_future = np.arange(steps).reshape(-1, 1)
    
    cpu_pred = cpu_model.predict(X_future) * 1.2
    ram_pred = ram_model.predict(X_future) * 1.15


    return cpu_pred, ram_pred