#!/bin/sh

python -m grpc_tools.protoc -I. --python_out=pyend/proto --grpc_python_out=pyend/proto core.proto
