# test_api.py
import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "temperature": 60,
    "humidity": 55,
    "sound": 75
}

response = requests.post(url, json=data)
print(response.json())
