# (part 1 :create sensor data which mimics realistic factory data)
import pandas as pd
import numpy as np

np.random.seed(42)

# Generate 1000 normal data points
temperature = np.random.normal(50, 5, 1000)
humidity = np.random.normal(50, 10, 1000)
sound = np.random.normal(70, 8, 1000)

# Inject 50 anomalies
anomalies = pd.DataFrame({
    'temperature': np.random.normal(90, 2, 50),
    'humidity': np.random.normal(90, 3, 50),
    'sound': np.random.normal(100, 5, 50)
})

# Combine data
normal = pd.DataFrame({
    'temperature': temperature,
    'humidity': humidity,
    'sound': sound
})

data = pd.concat([normal, anomalies], ignore_index=True)
data.to_csv('data/sensor_data.csv', index=False)
print("Simulated sensor data saved to data/sensor_data.csv!")
