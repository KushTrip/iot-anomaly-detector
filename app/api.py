from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join("..", "model", "model.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return "✅ IoT Anomaly Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()

        # Convert to DataFrame
        df = pd.DataFrame([input_data])

        # Predict (Isolation Forest returns 1 for normal, -1 for anomaly)
        pred = model.predict(df)[0]
        score = 0 if pred == 1 else 1  # 0 = normal, 1 = anomaly

        return jsonify({
            "anomaly_score": score,
            "status": "anomaly" if score == 1 else "normal"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
