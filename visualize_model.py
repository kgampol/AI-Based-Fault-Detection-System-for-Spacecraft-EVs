import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
import joblib
from datetime import datetime, timedelta

def generate_synthetic_data(n_samples=1000):
    """Generate synthetic sensor data with known patterns"""
    np.random.seed(42)
    
    # Generate time series data
    timestamps = [datetime.now() + timedelta(minutes=i) for i in range(n_samples)]
    
    # Generate normal sensor readings
    data = {
        'Temperature': np.random.normal(75, 5, n_samples),
        'Voltage': np.random.normal(12, 0.5, n_samples),
        'Vibration': np.random.normal(0.5, 0.1, n_samples),
        'Pressure': np.random.normal(30, 2, n_samples)
    }
    
    # Add some known fault patterns
    fault_indices = np.random.choice(n_samples, size=100, replace=False)
    
    # Temperature spikes
    data['Temperature'][fault_indices[:30]] += np.random.uniform(20, 40, 30)
    
    # Voltage drops
    data['Voltage'][fault_indices[30:60]] -= np.random.uniform(3, 7, 30)
    
    # Vibration spikes
    data['Vibration'][fault_indices[60:80]] += np.random.uniform(2, 4, 20)
    
    # Pressure anomalies
    data['Pressure'][fault_indices[80:]] += np.random.uniform(20, 40, 20)
    
    return pd.DataFrame(data, index=timestamps)

def plot_sensor_data(df, model_predictions, sensor_name):
    """Plot sensor data with model predictions"""
    plt.figure(figsize=(15, 8))
    
    # Create subplot for the main graph
    ax1 = plt.subplot(211)
    
    # Plot actual values
    plt.plot(df.index, df[sensor_name], 'b-', label='Sensor Readings', alpha=0.7)
    
    # Plot anomalies detected by the model
    anomaly_indices = model_predictions == -1
    plt.scatter(df.index[anomaly_indices], 
               df[sensor_name][anomaly_indices],
               color='red', label='AI Detected Anomalies', alpha=0.7)
    
    # Add threshold lines
    mean_val = df[sensor_name].mean()
    std_val = df[sensor_name].std()
    plt.axhline(y=mean_val + 2*std_val, color='g', linestyle='--', label='Upper Threshold')
    plt.axhline(y=mean_val - 2*std_val, color='g', linestyle='--', label='Lower Threshold')
    
    plt.title(f'{sensor_name} Sensor Analysis', fontsize=14, pad=20)
    plt.xlabel('Time')
    plt.ylabel(sensor_name)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    # Add explanation text
    explanation = f"""
    This graph shows:
    • Blue line: Actual {sensor_name} readings over time
    • Red dots: Anomalies detected by the AI model
    • Green lines: Statistical thresholds (±2 standard deviations)
    
    Normal Range: {mean_val - 2*std_val:.1f} to {mean_val + 2*std_val:.1f}
    Mean Value: {mean_val:.1f}
    Standard Deviation: {std_val:.1f}
    
    AI Model Detections: {sum(anomaly_indices)} anomalies
    """
    
    # Create subplot for explanation
    ax2 = plt.subplot(212)
    ax2.text(0.5, 0.5, explanation, 
             horizontalalignment='center',
             verticalalignment='center',
             transform=ax2.transAxes,
             fontsize=10)
    ax2.axis('off')
    
    plt.tight_layout()
    return plt.gcf()

def plot_correlation_heatmap(df):
    """Create an enhanced correlation heatmap with explanations"""
    plt.figure(figsize=(12, 10))
    
    # Create correlation matrix
    corr_matrix = df.corr()
    
    # Create heatmap
    sns.heatmap(corr_matrix, 
                annot=True, 
                cmap='coolwarm', 
                center=0,
                fmt='.2f',
                square=True)
    
    plt.title('Sensor Correlation Analysis', fontsize=14, pad=20)
    
    # Add explanation
    explanation = """
    This heatmap shows how different sensors correlate with each other:
    • Red: Strong positive correlation (sensors move together)
    • Blue: Strong negative correlation (sensors move oppositely)
    • White: No correlation
    
    Values range from -1 (perfect negative correlation) to 1 (perfect positive correlation)
    """
    
    plt.figtext(0.5, 0.02, explanation, 
                horizontalalignment='center',
                fontsize=10)
    
    plt.tight_layout()
    return plt.gcf()

def main():
    # Generate synthetic data
    print("Generating synthetic sensor data...")
    df = generate_synthetic_data()
    
    # Load the trained model
    print("Loading the trained model...")
    model = joblib.load('fault_detection_model.pkl')
    
    # Get model predictions
    print("Getting model predictions...")
    predictions = model.predict(df)
    
    # Create visualizations for each sensor
    sensors = ['Temperature', 'Voltage', 'Vibration', 'Pressure']
    for sensor in sensors:
        print(f"Creating visualization for {sensor}...")
        fig = plot_sensor_data(df, predictions, sensor)
        fig.savefig(f'{sensor.lower()}_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    # Create correlation heatmap
    print("Creating correlation heatmap...")
    fig = plot_correlation_heatmap(df)
    fig.savefig('sensor_correlations.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("\nActual Anomalies (based on thresholds):")
    for sensor in sensors:
        mean_val = df[sensor].mean()
        std_val = df[sensor].std()
        anomalies = df[abs(df[sensor] - mean_val) > 2*std_val]
        print(f"{sensor}: {len(anomalies)} anomalies detected")
    
    print("\nModel Predictions:")
    print(f"Total anomalies detected by model: {sum(predictions == -1)}")
    
    print("\nVisualization files created:")
    for sensor in sensors:
        print(f"- {sensor.lower()}_analysis.png")
    print("- sensor_correlations.png")

if __name__ == "__main__":
    main() 