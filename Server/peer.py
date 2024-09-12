from file import File
import requests
import asyncio 
class Peer:

    def __init__(self, client_id:str, ip:str, port:int, token:str) -> None:
        self.ip = ip
        self.port = port
        self.client_id = client_id
        self.token = token
        
    def __iter__(self) -> iter:
        return iter(self.fileList)