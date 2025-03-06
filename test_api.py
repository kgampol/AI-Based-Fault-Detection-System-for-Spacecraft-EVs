import requests
import time
import sys
import json

# Define the API endpoint
url = "http://127.0.0.1:5000/predict"

def wait_for_server(max_retries=5, delay=2):
    """Wait for the server to be ready"""
    for i in range(max_retries):
        try:
            # Try to connect to the health endpoint
            response = requests.get("http://127.0.0.1:5000/health")
            if response.status_code == 200:
                print("Server is ready!")
                return True
        except requests.exceptions.ConnectionError:
            print(f"Waiting for server... (attempt {i+1}/{max_retries})")
            time.sleep(delay)
    return False

# Define multiple test scenarios
test_scenarios = {
    "normal_conditions": {
        "Temperature": 75,    # Normal temperature
        "Voltage": 12,        # Normal voltage
        "Vibration": 0.5,     # Normal vibration
        "Pressure": 30        # Normal pressure
    },
    "high_temperature": {
        "Temperature": 145,   # Very high temperature
        "Voltage": 12,        # Normal voltage
        "Vibration": 0.5,     # Normal vibration
        "Pressure": 30        # Normal pressure
    },
    "low_voltage": {
        "Temperature": 75,    # Normal temperature
        "Voltage": 5,         # Very low voltage
        "Vibration": 0.5,     # Normal vibration
        "Pressure": 30        # Normal pressure
    },
    "high_vibration": {
        "Temperature": 75,    # Normal temperature
        "Voltage": 12,        # Normal voltage
        "Vibration": 4.8,     # Very high vibration
        "Pressure": 30        # Normal pressure
    },
    "high_pressure": {
        "Temperature": 75,    # Normal temperature
        "Voltage": 12,        # Normal voltage
        "Vibration": 0.5,     # Normal vibration
        "Pressure": 95        # Very high pressure
    },
    "multiple_issues": {
        "Temperature": 130,   # High temperature
        "Voltage": 8,         # Low voltage
        "Vibration": 3.5,     # High vibration
        "Pressure": 80        # High pressure
    }
}

def run_test(scenario_name, data):
    """Run a single test scenario"""
    print(f"\nTesting scenario: {scenario_name}")
    print("Sensor data:", json.dumps(data, indent=2))
    
    try:
        response = requests.post(url, json=data)
        result = response.json()
        
        print("\nAPI Response:")
        print(json.dumps(result, indent=2))
        print(f"Status Code: {response.status_code}")
        
        # Print a summary of the results
        if result.get('fault_detected'):
            print(f"⚠️ FAULT DETECTED! Confidence: {result['confidence_score']:.2f}")
        else:
            print(f"✅ No fault detected. Confidence: {result['confidence_score']:.2f}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the server. Make sure app.py is running.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error making request: {str(e)}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

def main():
    # Wait for server to be ready
    if not wait_for_server():
        print("Error: Server did not become ready in time")
        sys.exit(1)

    print("\n=== Starting Fault Detection System Tests ===\n")
    
    # Run all test scenarios
    for scenario_name, data in test_scenarios.items():
        run_test(scenario_name, data)
        time.sleep(1)  # Add a small delay between tests
    
    print("\n=== Test Suite Completed ===")

if __name__ == "__main__":
    main()
