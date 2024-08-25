import requests

api_url = "http://localhost:8000/predict"

# Make a prediction request
response = requests.post(api_url, json={"days": 30})

if response.status_code == 200:
    predictions = response.json()
    print(f"Received {len(predictions)} predictions.")
    print("First prediction:", predictions[0])
else:
    print("Error:", response.status_code, response.text)