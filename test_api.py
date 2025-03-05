import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/predict"

# Create a test JSON payload (simulated sensor readings)
data = {
    "Temperature": 100,  # High temp
    "Voltage": 9,  # Low voltage (potential failure)
    "Vibration": 1.5,  # High vibration
    "Pressure": 50  # High pressure
}

# Send a POST request to the API
response = requests.post(url, json=data)

# Print the API response
print("API Response:", response.json())
