from fastapi.testclient import TestClient
from stock_prediction_api.app.main import app

client = TestClient(app)

def test_predict():
    days_to_predict = 7
    print(f"\nRequesting prediction for {days_to_predict} days")
    response = client.post("/predict", json={"days": days_to_predict})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    predictions = response.json()
    print(f"Number of predictions returned: {len(predictions)}")
    print("Prediction dates:")
    for pred in predictions:
        print(pred['ds'])
    assert len(predictions) == days_to_predict, f"Expected {days_to_predict} predictions, but got {len(predictions)}"
    assert all(isinstance(p, dict) for p in predictions)
    assert all(set(p.keys()) == {"ds", "yhat", "yhat_lower", "yhat_upper"} for p in predictions)
