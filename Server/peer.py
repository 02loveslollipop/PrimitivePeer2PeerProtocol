from file import File
import requests
import asyncio 
from hashlib import sha256
class Peer:
    
    class Status:
        def __init__(self, status:bool,magicNumber: str) -> None:
            self.status = status
            self.Hash = sha256(string=magicNumber.encode()).hexdigest()
            
        def __bool__(self):
            return self.status
    
    def __init__(self, uri:str,ttl: int) -> None:
        self.uri = uri
        self.isAvailable = self.Status(True)
        self.statusCheckerInstance = asyncio.get_event_loop().create_task(self._statusChecker(uri, self.isAvailable, ttl))
        self.fileList = []
        
        
    def __iter__(self) -> iter:
        return iter(self.fileList)
    
    def addFile(self, file:str) -> None:
        self.fileList.append(File(file, self))

    @staticmethod
    async def _statusChecker(uri:str, status:bool,ttl:int) -> None:
        loop = True
        while loop:
            try:
                response = requests.get(f"{uri}/status")
                if response.status_code != 200:
                    status.status = False
                    loop = False
                await asyncio.sleep(ttl)
            except requests.exceptions.ConnectionError:
                status.status = False
                loop = False
            except Exception as e:
                print(e)
                status.status = False
                loop = False
            
        
    
    
