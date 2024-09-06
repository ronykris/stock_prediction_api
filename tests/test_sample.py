import requests

api_url = "http://127.0.0.1:8000/predict"

# Make a prediction request
response = requests.post(api_url, json={"days": 30})

if response.status_code == 200:
    predictions = response.json()
    print(f"Received {len(predictions)} predictions.")
    print("Predictions:", predictions)
else:
    print("Error:", response.status_code, response.text)