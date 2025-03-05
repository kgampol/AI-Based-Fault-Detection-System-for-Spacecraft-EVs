import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate time-series data (1000 readings)
time_steps = 1000
time = np.arange(time_steps)

# Generate normal sensor data
temperature = np.random.normal(75, 3, time_steps)  # Normal temp ~75°F
voltage = np.random.normal(12, 0.5, time_steps)  # Battery voltage ~12V
vibration = np.random.normal(0.3, 0.1, time_steps)  # Low vibration
pressure = np.random.normal(35, 2, time_steps)  # Normal pressure ~35 psi

# Introduce random failures (anomalies)
failure_indices = np.random.choice(time_steps, size=50, replace=False)  # 50 random failures

temperature[failure_indices] += np.random.randint(10, 20, size=50)  # Temp spikes
voltage[failure_indices] -= np.random.randint(2, 5, size=50)  # Voltage drops
vibration[failure_indices] += np.random.uniform(0.5, 1.5, size=50)  # High vibration
pressure[failure_indices] += np.random.uniform(-10, 10, size=50)  # Pressure fluctuations

# Create a failure label (1 = failure, 0 = normal)
labels = np.zeros(time_steps)
labels[failure_indices] = 1  # Mark anomalies

# Create DataFrame
df = pd.DataFrame({
    'Time': time,
    'Temperature': temperature,
    'Voltage': voltage,
    'Vibration': vibration,
    'Pressure': pressure,
    'Failure': labels  # 1 = failure, 0 = normal
})

# Save dataset
df.to_csv('synthetic_sensor_data.csv', index=False)
print("✅ Synthetic sensor data generated & saved as 'synthetic_sensor_data.csv'")
