import pandas as pd
import matplotlib.pyplot as plt

# Load synthetic dataset
df = pd.read_csv('AI-Based Fault Detection System for Spacecraft & EVs\synthetic_sensor_data.csv')

# Plot temperature with failure markers
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Temperature'], label="Temperature")
plt.scatter(df[df['Failure'] == 1]['Time'], df[df['Failure'] == 1]['Temperature'], color='red', label="Failures")
plt.xlabel("Time")
plt.ylabel("Temperature (°F)")
plt.legend()
plt.title("Temperature Sensor Readings Over Time")
plt.show()
