import asyncio
import grpc
import p2p_pb2_grpc
import p2p_pb2
from greeter_server import Greeter

class GRPCWorker:
    def __init__(self, server: grpc.Server, port: int, peerlist: list['Peer'], ttl: int) -> None:
        self.server = server
        self.port = port
        self.peerlist = peerlist
        self.ttl = ttl
        self.worker = asyncio.get_event_loop().create_task(self.start())
        

    def start(self) -> None:
        p2p_pb2_grpc.add_GreeterServicer_to_server(Greeter(self.peerlist,self.ttl), self.server)
        self.server.add_insecure_port(f'[::]:{self.port}')
        self.server.start()
        self.server.wait_for_termination()

    def stop(self) -> None:
        self.worker.cancel()