import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load the synthetic sensor dataset
df = pd.read_csv('AI-Based Fault Detection System for Spacecraft & EVs\synthetic_sensor_data.csv')

# Select sensor readings as features
features = ['Temperature', 'Voltage', 'Vibration', 'Pressure']
X = df[features]

# Train Isolation Forest Model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)

# Save Model
joblib.dump(model, 'fault_detection_model.pkl')

print("✅ AI model trained & saved as 'fault_detection_model.pkl'")
