import p2p_pb2_grpc
import p2p_pb2

class Greeter(p2p_pb2_grpc.GreeterServicer):

    def join(self, request, context):
        return p2p_pb2.HelloReply(message=f"Hello, {request.name}!")

    def leave(self, request, context):
        return p2p_pb2.HelloReply(message=f"Hello again, {request.name}!")