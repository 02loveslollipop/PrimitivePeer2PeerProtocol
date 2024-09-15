import requests
import os
from config import config
import grpc
from concurrent import futures
import p2p_pb2_grpc
from p2pServiceServicer import P2PServiceServicer
import random

class PeerServer:
    def __init__(self, path:str, config: config) -> None: 
        '''
        # PeerServer(*self*, path:str) -> None
        the constructor of the PeerServer class it initializes the Server side of the p2p peer, it will make availabe all the file in the path given as argument.
        ## Arguments
        path: str -> the path to the directory where the files are stored
        config: config -> the configuration object that contains the network configuration
        ## Returns
        None
        '''
        self.path = path
        
        if not os.path.exists(path): #if the path does not exist, use the current working directory
            self.path = os.getcwd()
        
        if not os.path.isdir(self.path): #if the path is not a directory, raise an error
            raise ValueError("Invalid path")
        
        #client_id is the name of the computer executing the code
        try:
            client_id = os.uname().nodename
        except AttributeError:
            client_id = str(random.randbytes(8).hex())
            
        
        #create the join request to the server
        joinRequest = {
            "client_id": client_id,
            "ip": config.ip,
            "port": config.control_port,
            "genericToken": config.token
        }
        request = requests.post(f"http://{config.ip}:{config.control_port}/register", json=joinRequest)
        if request.status_code == 200:
            self.token = request.json()['token']
        else:
            raise ValueError("Invalid token")

        #make all the files in path available in the server
        for file in os.listdir(self.path):
            self._addFile(self.token, file, config.ip, config.control_port)
    
    @staticmethod
    def _addFile(token:str, filename: str, host: str, port: int) -> None:
        '''
        # _addFile(token:str, filename: str, host: str) -> None
        add a file to the server
        ## Arguments
        token: str -> the token of the peer
        filename: str -> the name of the file to add
        host: str -> the host of the server
        ## Returns
        None
        '''
        json = {
            "file_name": filename,
            "token": token
        }
        request = requests.post(f"http://{host}:{port}/add_file", json=json)
        if request.status_code != 200:
            raise ValueError("Invalid token")
    
    def run(self) -> None:
        '''
        # run() -> None
        run the gRPC server
        ## Arguments
        None
        ## Returns
        None
        '''
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        p2p_pb2_grpc.add_GreeterServicer_to_server(P2PServiceServicer(self.path), server)
        server.add_insecure_port(f"[::]:{config.dataPort}")
        server.start()
        server.wait_for_termination()

    
        
        
        
        
        