# etcd-grpc
Auto-generated C++ gRPC API

## How to generate .h and .cc files from .proto files:
Protobuf-compiler must be installed and have appropriate version. Also, grpc-plugins needed for code generating.
```bash
	cd proto && \
	protoc -I . --grpc_out=../src/ --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ./rpc.proto &&\
	protoc -I . --cpp_out=../src/ ./*.proto && \
	cd -
```
