# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

import core_pb2 as core__pb2


class FraudDetectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PredictFraud = channel.unary_unary(
            "/fraud_detection.FraudDetectionService/PredictFraud",
            request_serializer=core__pb2.PredictionRequest.SerializeToString,
            response_deserializer=core__pb2.PredictionResponse.FromString,
        )


class FraudDetectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PredictFraud(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FraudDetectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PredictFraud": grpc.unary_unary_rpc_method_handler(
            servicer.PredictFraud,
            request_deserializer=core__pb2.PredictionRequest.FromString,
            response_serializer=core__pb2.PredictionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "fraud_detection.FraudDetectionService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FraudDetectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PredictFraud(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fraud_detection.FraudDetectionService/PredictFraud",
            core__pb2.PredictionRequest.SerializeToString,
            core__pb2.PredictionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
