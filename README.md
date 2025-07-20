# IoT Anomaly Detection (Stream Processing)

This project demonstrates a lightweight real-time anomaly detection system using simulated IoT sensor data. It was built for the IU module **DLBDSMTP01 – Project: From Model to Production**.

The system simulates live sensor readings from a smart factory, detects anomalies using a trained machine learning model (Isolation Forest), and serves predictions through a REST API built with Flask.

## 📁 Project Structure

```
iot-anomaly-detector/
│
├── app/
│   ├── api.py                # Flask API to serve the model
│   └── stream_simulator.py   # Simulates real-time sensor data stream
│
├── data/
│   └── sensor_data.csv       # Simulated sensor data (normal + anomalies)
│
├── model/
│   └── model.pkl             # Trained Isolation Forest model
│
├── generate_data.py          # Script to simulate and save sensor data
├── train_model.py            # Trains Isolation Forest and saves model
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview
```

## 🚀 How to Run

Follow these steps to set up and run the project:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/KushTrip/iot-anomaly-detector.git
   cd (copy the directory where this project will be saved)
   ```

2. **Install dependencies**  
It is extremely crucial to install the requirements for the system to work.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the following code in CMD to Generate the sensor data**

   ```bash
   cd (For Example: C:\Users\Username\Downloads\iot-anomaly-detector.git)
   ```
  
   ```bash
   python generate_data.py
   ```

4. **Run the following code in CMD to Train the anomaly detection model**  

   ```bash
   cd (For Example: C:\Users\Username\Downloads\iot-anomaly-detector.git)
   ```

   ```bash
   python train_model.py
   ```

5. **Run the following code in CMD to Start the REST API**

   ```bash
   cd (For Example: C:\Users\Username\Downloads\iot-anomaly-detector.git\app)
   ```
  
   ```bash
   python api.py
   ```
   You'll see the following output
```   
 * Serving Flask app 'api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 897-100-635
```
7. **Start the data stream simulator** 

   ```bash
   cd (For Example: C:\Users\Username\Downloads\iot-anomaly-detector.git\app)
   ```
 
   Run the following code in a separate terminal:
   ```bash
   python stream_simulator.py
   ```
   You'll see the following output
```   
🚀 Starting data stream simulation...

Reading 1: {
  'temperature': 52.48357076505616,
  'humidity': 63.99355436586002,
  'sound': 64.59857380020495
}
➡️ {'anomaly_score': 0, 'status': 'normal'}

Reading 2: {
  'temperature': 49.30867849414408,
  'humidity': 59.246336829127685,
  'sound': 68.84385063427585
}
➡️ {'anomaly_score': 0, 'status': 'normal'}

Reading 3: {
  'temperature': 53.23844269050346,
  'humidity': 50.59630369920174,
  'sound': 63.66064063200031
}
➡️ {'anomaly_score': 0, 'status': 'normal'}

```
and then reading 4, reading 5 and so on it goes. 
   

## 🧠 Model Info

- **Algorithm**: Isolation Forest (unsupervised anomaly detection)
- **Output**:  
  - `anomaly_score`: `0` (normal), `1` (anomaly) — simplified for readability  
  - `status`: "normal" or "anomaly"

> Although Isolation Forest internally returns -1 for anomalies and 1 for normal points, the API output is adjusted for clarity.

## 📊 Features Used

- `temperature`
- `humidity`
- `sound_volume`

## 📝 Notes

- Simulates 1050 total readings (1000 normal + 50 anomalies)
- Approximately 5% anomalies detected (53 out of 1050)
- Fully modular and reproducible codebase
- Beginner-friendly, but can be extended for Docker, CI/CD, or cloud deployment

---

**Project by Kush Tripathi**  
IU International University  
Module: DLBDSMTP01
