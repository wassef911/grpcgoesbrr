import pytest
import requests
from unittest.mock import ANY


@pytest.mark.timeout(0.5)  # 500ms
@pytest.mark.parametrize("execution_number", range(10))
def test_fraud_activity_api(execution_number):
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
