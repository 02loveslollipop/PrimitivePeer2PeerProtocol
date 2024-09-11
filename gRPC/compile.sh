python -m grpc_tools.protoc -I. --python_out=../Common --pyi_out=../Common --grpc_python_out=../Common ./p2p.proto
cp ../Common/p2p_pb2.py ../Peer/p2p_pb2.py
cp ../Common/p2p_pb2_grpc.py ../Peer/p2p_pb2_grpc.py
cp ../Common/p2p_pb2.pyi ../Peer/p2p_pb2.pyi
cp ../Common/p2p_pb2_grpc.py ../Server/p2p_pb2.py
cp ../Common/p2p_pb2_grpc.py ../Server/p2p_pb2_grpc.py
cp ../Common/p2p_pb2.pyi ../Server/p2p_pb2.pyi