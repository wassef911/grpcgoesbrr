import logging
import grpc
from concurrent import futures
from .proto.core_pb2_grpc import (
    FraudDetectionServiceServicer,
    add_FraudDetectionServiceServicer_to_server,
)
from .proto.core_pb2 import PredictionRequest, PredictionResponse
from .ml import HighlySuffincticatedModel
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

# Imagine these as env variables.
HOST = "::"
PORT = 50051
NUM_WORKERS = 2


class FraudServicer(FraudDetectionServiceServicer):
    def __init__(self, model: HighlySuffincticatedModel) -> None:
        super().__init__()
        self.model = model

    def PredictFraud(self, request: PredictionRequest, context) -> PredictionResponse:
        """
        int64 transaction_id = 1;
        double amount = 2;
        int64 time = 3;
        int32 age_of_account = 4;
        int32 number_of_transactions = 5;
        """
        result = self.model.predict(
            request.transaction_id,
            request.amount,
            request.time,
            request.age_of_account,
            request.number_of_transactions,
        )
        return PredictionResponse(result.model_dump(exclude_none=True))


class App:
    def __init__(self, pickle_path: str) -> None:
        self.fraud_model = HighlySuffincticatedModel(pickle_path)

    def run(self):
        logger.info("Starting server...")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

        add_FraudDetectionServiceServicer_to_server(
            FraudServicer(self.fraud_model), server
        )

        server.add_insecure_port(f"[{HOST}]:{PORT}")
        server.start()
        logger.info(f"🚀 Server is running on port {PORT}...")
        server.wait_for_termination()

    def tear_down(self):
        pass


if __name__ == "__main__":
    app = App("path/to/model.pkl")
    try:
        app.run()
    except Exception as exc:
        logger.error(f"Error: {exc}")
        app.tear_down()
