# Spacecraft & EV Fault Detection System

A production-grade AI-based fault detection system for spacecraft and electric vehicles, using real-time sensor data analysis.

## Features

- Real-time sensor data monitoring
- AI-powered anomaly detection
- RESTful API interface
- Prometheus metrics integration
- Comprehensive test suite
- Production-ready deployment configuration

## Installation

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

## Usage

1. Start the production server:
```bash
gunicorn app:app -b 0.0.0.0:5000
```

2. Send test data:
```bash
python test_api.py
```

## API Endpoints

- `POST /predict`: Submit sensor data for fault detection
- `GET /metrics`: Prometheus metrics endpoint
- `GET /health`: Health check endpoint

## Monitoring

The system includes Prometheus metrics for:
- Request latency
- Prediction accuracy
- System resource usage
- Fault detection rate

## Development

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

## Production Deployment

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

## License

Proprietary - All rights reserved
