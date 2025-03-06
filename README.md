# Spacecraft & EV Fault Detection System 🚀

A production-grade AI-based fault detection system designed for real-time monitoring of spacecraft and electric vehicles. This system uses advanced machine learning techniques to detect anomalies in sensor data, providing early warning of potential failures.

## 🎯 Main Purposes

1. **Real-time Monitoring**
   - Continuous monitoring of critical sensor data
   - Instant detection of anomalies and potential failures
   - Early warning system for preventive maintenance

2. **Fault Detection**
   - AI-powered anomaly detection using Isolation Forest algorithm
   - Multi-sensor data analysis (Temperature, Voltage, Vibration, Pressure)
   - Confidence scoring for detected anomalies

3. **Production Readiness**
   - Enterprise-grade monitoring and logging
   - Scalable containerized deployment
   - Comprehensive test coverage
   - Production-grade security measures

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.11**: Main programming language
- **Flask**: Web framework for API development
- **Scikit-learn**: Machine learning library for anomaly detection
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

### Monitoring & Logging
- **Prometheus**: Metrics collection and monitoring
- **Logging**: Structured application logging

### Development & Testing
- **Pytest**: Testing framework
- **Black**: Code formatting
- **Flake8**: Code linting

### Deployment & Containerization
- **Docker**: Containerization
- **Gunicorn**: Production-grade WSGI server

## 📊 System Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Sensor Data   │     │   API Server    │     │  AI Model      │
│   Collection    │ ──> │   (Flask)       │ ──> │  (Isolation    │
│                 │     │                 │     │   Forest)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                      │                        │
         │                      │                        │
         ▼                      ▼                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Data          │     │   Prometheus    │     │   Fault        │
│   Validation    │     │   Metrics       │     │   Detection    │
│                 │     │                 │     │   Results      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## 📦 Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd spacecraft-fault-detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🛠️ Usage

### Running the API Server

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000`

### Testing the API

```bash
python test_api.py
```

### Visualizing Sensor Data and Model Performance

```bash
python visualize_model.py
```

This will generate several visualization files:
- `temperature_analysis.png`: Temperature sensor readings and anomaly detection
- `voltage_analysis.png`: Voltage sensor readings and anomaly detection
- `vibration_analysis.png`: Vibration sensor readings and anomaly detection
- `pressure_analysis.png`: Pressure sensor readings and anomaly detection
- `sensor_correlations.png`: Correlation analysis between different sensors

## Using Real Sensor Data

To use your own sensor data instead of synthetic data:

1. Prepare your sensor data in CSV format with the following columns:
   ```
   Temperature,Voltage,Vibration,Pressure
   75.2,12.1,0.5,30.1
   76.1,12.0,0.4,30.2
   ...
   ```

2. Modify the `train_ai_model.py` script to use your data:
   ```python
   # Replace this line in train_ai_model.py
   df = pd.read_csv('your_sensor_data.csv')
   ```

3. Retrain the model:
   ```bash
   python train_ai_model.py
   ```

4. Run the visualization script to analyze your data:
   ```bash
   python visualize_model.py
   ```

## Visualization Guide

### Individual Sensor Analysis Plots

Each sensor plot (`temperature_analysis.png`, etc.) shows:
- Blue line: Actual sensor readings over time
- Red dots: Anomalies detected by the AI model
- Green dashed lines: Statistical thresholds (±2 standard deviations)
- Detailed statistics including:
  - Normal operating range
  - Mean value
  - Standard deviation
  - Number of anomalies detected

### Correlation Heatmap

The `sensor_correlations.png` shows relationships between sensors:
- Red: Strong positive correlation (sensors move together)
- Blue: Strong negative correlation (sensors move oppositely)
- White: No correlation
- Values range from -1 to 1

## API Endpoints

### Health Check
```
GET /health
```

### Fault Detection
```
POST /predict
Content-Type: application/json

{
    "Temperature": 75.0,
    "Voltage": 12.0,
    "Vibration": 0.5,
    "Pressure": 30.0
}
```

Response:
```json
{
    "fault_detected": false,
    "confidence_score": 0.51,
    "sensor_values": {
        "Temperature": 75.0,
        "Voltage": 12.0,
        "Vibration": 0.5,
        "Pressure": 30.0
    }
}
```

## Model Training

The system uses an Isolation Forest algorithm for anomaly detection. The model is trained on:
- Normal sensor readings
- Known fault patterns
- Statistical thresholds

To retrain the model with new data:
1. Update the training data in `train_ai_model.py`
2. Run the training script
3. The new model will be saved as `fault_detection_model.pkl`

## 🚀 Production Deployment

1. Deploy using Docker:
```bash
docker build -t fault-detection .
docker run -p 5000:5000 fault-detection
```

## 📝 License

Proprietary - All rights reserved

## 👥 Contributing

This is a proprietary system developed for spacecraft and EV fault detection. For inquiries about collaboration or licensing, please contact the repository owner.
