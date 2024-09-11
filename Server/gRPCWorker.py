import asyncio
import grpc

class GRPCWorker:
    def __init__(self, server: grpc.Server, port: int) -> None:
        self.server = server
        self.port = port
        self.worker = asyncio.get_event_loop().create_task(self.start())
        

    def start(self) -> None:
        self.server.add_insecure_port(f'[::]:{self.port}')
        self.server.start()
        self.server.wait_for_termination()

    def stop(self) -> None:
        self.worker.cancel()