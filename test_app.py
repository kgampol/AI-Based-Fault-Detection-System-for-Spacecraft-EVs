import pytest
import requests
import json
import time

BASE_URL = "http://127.0.0.1:5000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_valid_prediction():
    data = {
        "Temperature": 75,
        "Voltage": 12,
        "Vibration": 0.3,
        "Pressure": 35
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 200
    result = response.json()
    assert "fault_detected" in result
    assert "confidence_score" in result
    assert "sensor_values" in result

def test_invalid_data():
    data = {
        "Temperature": "invalid",
        "Voltage": 12,
        "Vibration": 0.3,
        "Pressure": 35
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 400
    assert "error" in response.json()

def test_missing_fields():
    data = {
        "Temperature": 75,
        "Voltage": 12
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 400
    assert "error" in response.json()

def test_out_of_range_values():
    data = {
        "Temperature": 200,  # Out of range
        "Voltage": 12,
        "Vibration": 0.3,
        "Pressure": 35
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 400
    assert "error" in response.json()

def test_metrics_endpoint():
    response = requests.get(f"{BASE_URL}/metrics")
    assert response.status_code == 200
    assert "fault_detection_predictions_total" in response.text
    assert "fault_detection_latency_seconds" in response.text
    assert "fault_detection_faults_total" in response.text 