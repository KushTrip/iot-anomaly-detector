import pandas as pd
import time
import requests
import os

# Load the data
data_path = os.path.join("..", "data", "sensor_data.csv")
df = pd.read_csv(data_path)

url = "http://127.0.0.1:5000/predict"

print("🚀 Starting data stream simulation...\n")

# Simulate streaming
for i, row in df.iterrows():
    data = {
        "temperature": row["temperature"],
        "humidity": row["humidity"],
        "sound": row["sound"]
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()

        print(f"Reading {i+1}: {{\n  'temperature': {data['temperature']},\n  'humidity': {data['humidity']},\n  'sound': {data['sound']}\n}} \n➡️ {result}\n")

    except Exception as e:
        print(f"❌ Error at reading {i+1}: {e}")

    time.sleep(1)  # Simulate real-time (1 second between readings)