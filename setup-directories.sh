#!/bin/bash

# pulse.ai Setup script
# This script creates the necessary directories for pulse.ai to store data and AI models.
# Run this BEFORE "docker-compose up"

echo "----------------------------------------------------"
echo "🚀 Setting up directories for pulse.ai System..."
echo "----------------------------------------------------"

# 1. AI & MLOps Directories
mkdir -p artifacts
mkdir -p mlruns  
mkdir -p mlflow_db
mkdir -p data/raw
mkdir -p data/processed

# 2. Monitoring & Database Persistence Directories
# These store Grafana dashboards, metrics, and time-series data
mkdir -p data/grafana
mkdir -p data/prometheus
mkdir -p data/influxdb

# 3. Set Permissions (Docker-safe for macOS)
# 775 allows Docker containers to write without exposing full public access
chmod -R 775 data
chmod -R 775 artifacts mlruns mlflow_db

# Get current user info (for logging/debugging)
USER_ID=$(id -u)
GROUP_ID=$(id -g)

echo "✅ Directories created successfully:"
echo "   - artifacts/       (AI Model Storage)"
echo "   - mlruns/          (MLflow Experiment Tracking)"  
echo "   - mlflow_db/       (MLflow Backend Database)"
echo "   - data/grafana     (Grafana Dashboards)"
echo "   - data/prometheus  (Prometheus Metrics)"
echo "   - data/influxdb    (Time-Series Database)"
echo ""
echo "👤 Current user: $(whoami) (UID: $USER_ID, GID: $GROUP_ID)"
echo "----------------------------------------------------"
echo "👉 Next Step: Run 'docker-compose up -d'"
echo "----------------------------------------------------"
