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
- **Python-dotenv**: Environment variable management
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

## 🚀 Features

- **Real-time Monitoring**
  - Live sensor data processing
  - Instant anomaly detection
  - Confidence scoring

- **Production Features**
  - Prometheus metrics integration
  - Comprehensive logging
  - Health check endpoints
  - Input validation
  - Error handling
  - Docker support

- **Development Tools**
  - Comprehensive test suite
  - Code formatting
  - Linting
  - Dependency management

## 📦 Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd spacecraft-fault-detection
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🛠️ Usage

1. Start the production server:
```bash
gunicorn app:app -b 0.0.0.0:5000
```

2. Send test data:
```bash
python test_api.py
```

## 🔌 API Endpoints

- `POST /predict`: Submit sensor data for fault detection
- `GET /metrics`: Prometheus metrics endpoint
- `GET /health`: Health check endpoint

## 📊 Monitoring

The system includes Prometheus metrics for:
- Request latency
- Prediction accuracy
- System resource usage
- Fault detection rate

## 🧪 Development

1. Run tests:
```bash
pytest
```

2. Format code:
```bash
black .
```

3. Lint code:
```bash
flake8
```

## 🚀 Production Deployment

1. Set environment variables:
```bash
export MODEL_PATH=/path/to/model.pkl
export LOG_LEVEL=INFO
```

2. Deploy using Docker:
```bash
docker build -t fault-detection .
docker run -p 5000:5000 fault-detection
```

## 📝 License

Proprietary - All rights reserved

## 👥 Contributing

This is a proprietary system developed for spacecraft and EV fault detection. For inquiries about collaboration or licensing, please contact the repository owner.
