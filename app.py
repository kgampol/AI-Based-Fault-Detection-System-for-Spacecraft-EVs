from flask import Flask, request, jsonify
import pandas as pd
import joblib
from typing import Dict, Any
import numpy as np
import logging
import os
import time

# Configure logging
logging.basicConfig(
    level='INFO',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load trained AI model
try:
    model_path = 'fault_detection_model.pkl'
    model = joblib.load(model_path)
    logger.info(f"Model loaded successfully from {model_path}")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    raise

# Define expected sensor ranges
SENSOR_RANGES = {
    'Temperature': {'min': 0, 'max': 150},  # °F
    'Voltage': {'min': 0, 'max': 15},      # V
    'Vibration': {'min': 0, 'max': 5},     # mm/s
    'Pressure': {'min': 0, 'max': 100}     # psi
}

def validate_sensor_data(data: Dict[str, Any]) -> tuple[bool, str]:
    """
    Validate the input sensor data.
    Returns (is_valid, error_message)
    """
    # Check for required fields
    required_fields = ['Temperature', 'Voltage', 'Vibration', 'Pressure']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"

    # Check data types and ranges
    for field, value in data.items():
        # Check if value is numeric
        try:
            float_value = float(value)
        except (ValueError, TypeError):
            return False, f"Field '{field}' must be numeric"

        # Check if value is within expected range
        if field in SENSOR_RANGES:
            if not (SENSOR_RANGES[field]['min'] <= float_value <= SENSOR_RANGES[field]['max']):
                return False, f"Field '{field}' value {float_value} is outside valid range [{SENSOR_RANGES[field]['min']}, {SENSOR_RANGES[field]['max']}]"

    return True, ""

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400

        # Receive JSON data
        data = request.get_json()
        logger.info(f"Received prediction request with data: {data}")
        
        # Validate input data
        is_valid, error_message = validate_sensor_data(data)
        if not is_valid:
            logger.warning(f"Invalid input data: {error_message}")
            return jsonify({'error': error_message}), 400

        # Convert JSON to Pandas DataFrame
        df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(df)[0]
        
        # Calculate confidence score (distance from decision boundary)
        confidence = abs(model.score_samples(df)[0])
        
        # Log the prediction
        if prediction == -1:
            logger.warning(f"Fault detected with confidence: {confidence}")
        else:
            logger.info(f"No fault detected with confidence: {confidence}")
        
        # Return response with confidence score
        return jsonify({
            'fault_detected': True if prediction == -1 else False,
            'confidence_score': float(confidence),
            'sensor_values': data
        })

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
