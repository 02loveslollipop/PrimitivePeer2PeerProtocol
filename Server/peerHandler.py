import threading
from peer import Peer
from file import File
from config import config
import requests

class PeerHandler:
    
    def __init__(self, ttl:int) -> None:
        self.ttl = ttl
        self.peerList = []
        self.fileList = []
                
    def removePeerFiles(self,client_id: str) -> None:
        for file in self.fileList:
            if file.Peer.client_id == client_id:
                self.fileList.remove(file)
                       
    def addFile(self, filename: str, token: str) -> None:
        for peer in self.peerList:
            if peer.token == token:
                newFile = File(filename, peer)
                self.fileList.append(newFile)
    
    def addPeer(self,client_id: str, ip: str, port: int, token: str) -> None:
        newPeer = Peer(client_id, ip, port,token)
        self.peerList.append(newPeer)
        
    def removePeer(self,token: str) -> None:
        for peer in self.peerList:
            if peer.token == token:
                client_id = peer.client_id
                self.peerList.remove(peer)
        
        self.removePeerFiles(client_id)

    def getFileList(self) -> list[str]:
        fileList = []
        for file in self.fileList:
            fileList.append(file.filename)
        return fileList

    def getFileAddress(self, filename: str) -> str | None: #TODO: when calling this method, check if the return value is None to return a 404
        for file in self.fileList:
            if file.filename == filename:
                return f"http://{file.Peer.ip}:{file.Peer.port}/{filename}"
        return None
    
    def authPeer(self, token: str) -> bool:
        for peer in self.peerList:
            if peer.token == token:
                return True
        return False
    
    def peerExists(self, client_id: str) -> bool:
        for peer in self.peerList:
            if peer.client_id == client_id:
                return True
        return False
    
    

