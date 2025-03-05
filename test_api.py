import requests
import time

# Define the API endpoint
url = "http://127.0.0.1:5000/predict"

# Wait for server to be ready
print("Waiting for server to be ready...")
time.sleep(2)

# Create a test JSON payload (simulated sensor readings)
data = {
    "Temperature": 100,  # High temp
    "Voltage": 9,  # Low voltage (potential failure)
    "Vibration": 1.5,  # High vibration
    "Pressure": 50  # High pressure
}

try:
    # Send a POST request to the API
    print("Sending test data...")
    response = requests.post(url, json=data)
    
    # Print the API response
    print("\nAPI Response:", response.json())
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server. Make sure app.py is running.")
except Exception as e:
    print(f"Error: {str(e)}")
