import grpc
from pyend.proto.core_pb2_grpc import (
    FraudDetectionServiceServicer,
    add_FraudDetectionServiceServicer_to_server,
)
from pyend.app import FraudServicer, HighlySophisticatedModel


async def stub():
    servicer = FraudServicer(HighlySophisticatedModel("path/to/model.pkl"))
    server = grpc.aio.server()
    add_FraudDetectionServiceServicer_to_server(servicer, server)
    channel = grpc.aio.insecure_channel("[::]:50051")
    await server.start()
    fraud_stub = FraudDetectionServiceServicer(channel)
    return fraud_stub


# @pytest.mark.asyncio
# async def test_predict_fraud():
#     actual_stub = await stub()
#     request = PredictionRequest(
#         transaction_id=1,
#         amount=100.0,
#         time=1234567890,
#         age_of_account=365,
#         number_of_transactions=5,
#     )
#     response = await actual_stub.PredictFraud(request)
#     assert response == 1, "The response value should be 1"


# def test_predict_fraud():
#     model = HighlySophisticatedModel("random/path/to/model.pkl")
#     app = App(model)

#     thread = threading.Thread(target=app.run)
#     thread.start()

#     target = "localhost:50051"
#     channel = grpc.insecure_channel(target)
#     stub = FraudDetectionServiceStub(channel)

#     try:
#         request = PredictionRequest(
#             transaction_id=1,
#             amount=100.0,
#             time=1234567890,
#             age_of_account=365,
#             number_of_transactions=5,
#         )

#         response = stub.PredictFraud(request)
#         assert response.transaction_id == 1, "Transaction ID should match the request"
#     finally:
#         channel.close()
#         app.stop()
#         thread.join()
