import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from model_predict import predict_future
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Pulse.ai",
    page_icon="📊",
    layout="wide"
)

PROMETHEUS_URL = "http://prometheus:9090"

# -----------------------------
# Helper Functions
# -----------------------------
def query_prometheus(query):
    url = f"{PROMETHEUS_URL}/api/v1/query"
    response = requests.get(url, params={"query": query})
    if response.status_code == 200:
        return response.json()["data"]["result"]
    return []

def get_cpu_usage():
    query = """
    100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)
    """
    result = query_prometheus(query)
    if result:
        return float(result[0]["value"][1])
    return None

def get_ram_usage():
    query = """
    (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
    """
    result = query_prometheus(query)
    if result:
        return float(result[0]["value"][1])
    return None

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("💡 Pulse.ai")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Monitoring", "🤖 AI Forecasting", "ℹ️ About"]
)

# -----------------------------
# Home Page
# -----------------------------
if page == "🏠 Home":
    st.title("🚀 Pulse.ai")
    st.subheader("Server Monitoring & AI Forecasting System")

    st.markdown("""
    **Pulse.ai** is a full-stack observability platform that:
    - Monitors system metrics in real time
    - Stores historical performance data
    - Uses AI to predict future load
    """)

# -----------------------------
# Monitoring Page (Grafana Embed)
# -----------------------------
elif page == "📊 Monitoring":
    st.title("📊 Live Server Monitoring")

    GRAFANA_DASHBOARD_UID = "rYdddlPWk"  # Node Exporter Full UID

    grafana_url = (
        f"http://localhost:3000/d/{GRAFANA_DASHBOARD_UID}"
        "?orgId=1&refresh=5s&kiosk"
    )

    st.components.v1.iframe(
        grafana_url,
        height=900,
        scrolling=True
    )

# -----------------------------
# AI Forecasting (PHASE 4 DATA)
# -----------------------------
elif page == "🤖 AI Forecasting":
    st.title("🤖 AI Forecasting – Next 10 Minutes")

    st.markdown("""
    This section uses **trained machine learning models**
    to predict future system load based on historical data.
    """)

    with st.spinner("Running AI prediction..."):
        cpu_pred, ram_pred = predict_future(steps=10)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted CPU Usage (avg)",
            f"{cpu_pred.mean():.2f} %"
        )

    with col2:
        st.metric(
            "Predicted RAM Usage (avg)",
            f"{ram_pred.mean():.2f} %"
        )

    st.subheader("📈 Predicted System Load Trend")

    pred_df = {
        "CPU Usage (%)": cpu_pred,
        "RAM Usage (%)": ram_pred
    }

    st.line_chart(pred_df)

    st.success("Prediction generated using trained ML models")
# -----------------------------
# About Page
# -----------------------------
elif page == "ℹ️ About":
    st.title("ℹ️ About Pulse.ai")

    st.markdown("""
    **Pulse.ai** is a final-year, industry-grade system combining:

    - Prometheus (metrics)
    - Grafana (visualization)
    - InfluxDB (time-series storage)
    - Machine Learning (forecasting)
    - Streamlit (full-stack UI)
    """)
    