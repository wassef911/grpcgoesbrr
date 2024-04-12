import pytest
import threading
import grpc
from pyend.proto.core_pb2 import PredictionRequest
from pyend.proto.core_pb2_grpc import FraudDetectionServiceStub
from pyend.app import App, HighlySophisticatedModel


@pytest.fixture(scope="module")
def app_fixture():
    model = HighlySophisticatedModel("random/path/to/model.pkl")
    app = App(model)

    thread = threading.Thread(target=app.run)
    thread.start()

    yield app

    app.stop()
    thread.join()


def test_predict_fraud(app_fixture):
    target = "localhost:50051"
    options = [
        ("grpc.lb_policy_name", "pick_first"),
        ("grpc.enable_retries", 0),
        ("grpc.keepalive_timeout_ms", 10000),
    ]
    channel = grpc.insecure_channel(target, options=options)
    stub = FraudDetectionServiceStub(channel)

    try:
        request = PredictionRequest(
            transaction_id=1,
            amount=100.0,
            time=1234567890,
            age_of_account=365,
            number_of_transactions=5,
        )

        response = stub.PredictFraud(request)
        assert response.transaction_id == 1, "Transaction ID should match the request"
    finally:
        channel.close()
