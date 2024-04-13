# test_fraud_activity.py

import requests
from unittest.mock import ANY


def test_fraud_activity_api():
    url = "http://localhost:8000/api/FraudActivity"
    params = {"transaction_id": "123456"}
    response = requests.get(url, params=params)
    assert (
        response.status_code == 200
    ), f"Expected status code 200, got {response.status_code}"
    expected_response = {
        "transaction_id": "123456",
        "predicted_label": ANY,
        "fraud_probability": ANY,
    }
    assert (
        response.json() == expected_response
    ), "Response data does not match expected data"
