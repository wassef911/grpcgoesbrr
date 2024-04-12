import logging
import grpc
from concurrent import futures
from .proto.core_pb2_grpc import (
    FraudDetectionServiceServicer,
    add_FraudDetectionServiceServicer_to_server,
)
from .proto.core_pb2 import PredictionRequest, PredictionResponse, DESCRIPTOR
from .ml import HighlySophisticatedModel
from grpc_reflection.v1alpha import reflection

logger = logging.getLogger(__name__)

# Imagine these as env variables.
HOST = "::"
PORT = 50051
NUM_WORKERS = 1


class FraudServicer(FraudDetectionServiceServicer):
    def __init__(self, model: HighlySophisticatedModel) -> None:
        super().__init__()
        self.model = model

    def PredictFraud(self, request: PredictionRequest, context) -> PredictionResponse:
        result = self.model.predict(
            request.transaction_id,
            request.amount,
            request.time,
            request.age_of_account,
            request.number_of_transactions,
        )
        context.set_code(grpc.StatusCode.OK)
        return PredictionResponse(**result.model_dump(exclude_none=True))


class App:
    def __init__(self, fraud_model: HighlySophisticatedModel) -> None:
        self.fraud_model = fraud_model
        self.server = None

    def run(self):
        logger.info("Starting server...")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=NUM_WORKERS))

        add_FraudDetectionServiceServicer_to_server(
            FraudServicer(self.fraud_model), server
        )

        SERVICE_NAMES = (
            DESCRIPTOR.services_by_name["FraudDetectionService"].full_name,
            reflection.SERVICE_NAME,
        )
        reflection.enable_server_reflection(SERVICE_NAMES, server)
        server.add_insecure_port(f"[{HOST}]:{PORT}")
        server.start()
        logger.info(f"🚀 Server is running on port {PORT}...")
        server.wait_for_termination()

    def stop(self):
        if self.server is not None:
            logger.info("Stopping the server...")
            self.server.stop(0)
            logger.info("Server has been stopped.")
