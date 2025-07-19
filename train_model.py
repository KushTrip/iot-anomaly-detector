import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Load data
data_path = os.path.join("data", "sensor_data.csv")
df = pd.read_csv(data_path)

# Train Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
model.fit(df)

# Save model
model_path = os.path.join("model", "model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained and saved to model/model.pkl")

# Predict on training data to check stats
predictions = model.predict(df)

# Count anomalies
normal_count = (predictions == 1).sum()
anomaly_count = (predictions == -1).sum()
total = len(predictions)

print("\n📊 Model Stats:")
print(f"Normal: {normal_count}")
print(f"Anomalies: {anomaly_count}")
print(f"Anomaly Ratio: {anomaly_count / total:.2%}")