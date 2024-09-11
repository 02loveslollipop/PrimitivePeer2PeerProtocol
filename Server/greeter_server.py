import p2p_pb2
import p2p_pb2_grpc
import grpc
from peer import Peer

class Greeter(p2p_pb2_grpc.GreeterServicer):
    
    def __init__(self, peerList: list,ttl: int) -> None:
        self.peerList = peerList
        self.ttl = ttl

    def join(self, request, context):
        """Join the p2p network
        """
        print(f"Peer {request.peerId} joined the network")
        self.peerList.append(Peer(uri=request.uri, ttl=self.ttl))
        context.set_code(grpc.StatusCode.OK)
        return p2p_pb2.connectionReply(status=True)

    def leave(self, request, context):
        """Leave the p2p network
        """
        for peer in self.peerList:
            if peer.Hash == request.hash:
                self.peerList.remove(peer)
                context.set_code(grpc.StatusCode.OK)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return p2p_pb2.connectionReply(status=False)
        return p2p_pb2.connectionReply(status=True)