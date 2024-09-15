import requests
import os
from config import config
import grpc
from concurrent import futures
import p2p_pb2
import p2p_pb2_grpc
from p2pServiceServicer import P2PServiceServicer

class PeerClient:
    def __init__(self, config: config) -> None:
        '''
        # PeerClient(*self*, config: config) -> None
        the constructor of the PeerClient class it initializes the client side of the p2p peer, it will make availabe all the file in the path given as argument.
        ## Arguments
        config: config -> the configuration object that contains the network configuration
        ## Returns
        None
        '''
        self.config = config

    def register(self) -> None:
        '''
        # register(*self*) -> None
        register the peer to the server
        ## Arguments
        None
        ## Returns
        None
        '''
        client_id = f"{os.uname().nodename}Client"
        json = {
            "client_id": client_id,
            "ip": self.config.ip,
            "port": self.config.dataPort,
            "genericToken": self.config.token
        }
        request = requests.post(f"http://{self.config.ip}:{self.config.control_port}/register", json=json)
        if request.status_code == 200:
            self.token = request.json()['token']
        else:
            raise ValueError("Could not register in the server")
    
    def unregister(self) -> None:
        '''
        # unregister(*self*) -> None
        unregister the peer from the server
        ## Arguments
        None
        ## Returns
        None
        '''
        json = {
            "token": self.token
        }
        request = requests.post(f"http://{self.config.ip}:{self.config.control_port}/unregister", json=json)
        if request.status_code == 200:
            token = None
            
        else:
            raise ValueError("Invalid token")   
        
    def getFileList(self) -> list[str]:
        '''
        # getFileList(*self*) -> list[str]
        get the list of files available in the server
        ## Arguments
        None
        ## Returns
        list[str] -> the list of files available in the server
        '''
        json = {
            "token": self.token
        }
        request = requests.get(f"http://{self.config.ip}:{self.config.control_port}/get_files", json=json)
        if request.status_code == 200:
            return request.json()['files']
        else:
            raise ValueError("Invalid token")
    
    def getFile(self, filename: str) -> str:
        '''
        # getFile(*self*, filename: str) -> str
        get the file from the server
        ## Arguments
        filename: str -> the name of the file to get
        ## Returns
        str -> the file content
        '''
        json = {
            "token": self.token,
            "file_name": filename
        }
        request = requests.get(f"http://{self.config.ip}:{self.config.control_port}/get_file", json=json)
        if request.status_code == 200:
            return request.json()['file_address']
        else:
            raise ValueError("Invalid token")
        
    def getBinaryFile(self, filename: str) -> bytes:
        '''
        # getBinaryFile(*self*, filename: str) -> bytes
        get the binary file from the server
        ## Arguments
        filename: str -> the name of the file to get
        ## Returns
        bytes -> the file content
        '''
        #filename is an URL of a structure like this: grpc://{host}:{port}/{file_name}
        #Note: {file_name} may contain '/'. Example: grpc://localhost:50051/folder1/file1
        #parse the URL
        print(filename) #TODO: remove this
        host = filename.split("//")[1].split(":")[0]
        port = int(filename.split(":")[2].split("/")[0])
        print(filename)
        pathArray = filename.split(":")[2].split("/")
        pathArray.pop(0)
        path_to_file = ""
        for path in pathArray:
            path_to_file += path + "/"
        path_to_file = path_to_file[:-1]

        #start the gRPC client
        channel = grpc.insecure_channel(f"{host}:{port}")
        stub = p2p_pb2_grpc.GreeterStub(channel)
        response = stub.getFile(p2p_pb2.fileRequest(file_path=path_to_file))
        #check if context.set_code(grpc.StatusCode.NOT_FOUND)
        return response.file_bytes
        
        