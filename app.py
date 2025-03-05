from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained AI model
model = joblib.load(r'AI-Based Fault Detection System for Spacecraft & EVs\fault_detection_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Receive JSON data
    data = request.get_json()

    # Convert JSON to Pandas DataFrame
    df = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(df)[0]
    
    # Return response
    return jsonify({'fault_detected': True if prediction == -1 else False})

if __name__ == '__main__':
    app.run(debug=True)
