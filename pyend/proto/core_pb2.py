# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ncore.proto\x12\x0f\x66raud_detection"\x81\x01\n\x11PredictionRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x03\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\x16\n\x0e\x61ge_of_account\x18\x04 \x01(\x05\x12\x1e\n\x16number_of_transactions\x18\x05 \x01(\x05"`\n\x12PredictionResponse\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x03\x12\x17\n\x0fpredicted_label\x18\x02 \x01(\x08\x12\x19\n\x11\x66raud_probability\x18\x03 \x01(\x01\x32p\n\x15\x46raudDetectionService\x12W\n\x0cPredictFraud\x12".fraud_detection.PredictionRequest\x1a#.fraud_detection.PredictionResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "core_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS is False:
    DESCRIPTOR._options = None
    _globals["_PREDICTIONREQUEST"]._serialized_start = 32
    _globals["_PREDICTIONREQUEST"]._serialized_end = 161
    _globals["_PREDICTIONRESPONSE"]._serialized_start = 163
    _globals["_PREDICTIONRESPONSE"]._serialized_end = 259
    _globals["_FRAUDDETECTIONSERVICE"]._serialized_start = 261
    _globals["_FRAUDDETECTIONSERVICE"]._serialized_end = 373
# @@protoc_insertion_point(module_scope)
