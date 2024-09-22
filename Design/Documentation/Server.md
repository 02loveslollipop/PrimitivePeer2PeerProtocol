# Overview
This P2P server allows peers to register, unregister, and manage files. It uses Flask for the web server and supports various endpoints for peer and file management.

# Configuration
The server configuration is stored in [`config.yaml`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/config.yaml):
```yaml
port: 8000 # Port to listen for incoming control messages
peer:
  port: 8001 # Port to listen for incoming data or to request data
auth:
  token: "secret" # Token to authenticate
```

# Endpoints

### Register a Peer
**URL:** `/register`  
**Method:** [`POST`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L20)  
**Description:** Registers a peer in the server and returns a token for future requests.

**Expected JSON:**
```json
{
    "client_id": "string",
    "ip": "string",
    "port": int,
    "genericToken": "string"
}
```

**Responses:**
- **200 OK:**
  ```json
  {
      "token": "string"
  }
  ```
- **400 Bad Request:**
  ```json
  {
      "message": "Peer already registered"
  }
  ```
- **401 Unauthorized:**
  ```json
  {
      "message": "Invalid token"
  }
  ```

## Unregister a Peer
**URL:** `/unregister`  
**Method:** [`POST`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L69)  
**Description:** Unregisters a peer and removes all associated files.

**Expected JSON:**
```json
{
    "token": "string"
}
```

**Responses:**
- **200 OK:**
  ```json
  {
      "message": "Peer unregistered"
  }
  ```
- **404 Not Found:**
  ```json
  {
      "message": "Invalid request"
  }
  ```
- **404 Not Found:**
  ```json
  {
      "message": "Peer not found"
  }
  ```

## Add a File
**URL:** `/add_file`  
**Method:** [`POST`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L107)  
**Description:** Adds a file to the server.

**Expected JSON:**
```json
{
    "token": "string",
    "file_name": "string"
}
```

**Responses:**
- **200 OK:**
  ```json
  {
      "message": "File added"
  }
  ```
- **400 Bad Request:**
  ```json
  {
      "message": "Invalid request"
  }
  ```
- **404 Not Found:**
  ```json
  {
      "message": "Peer not found"
  }
  ```

## Get Files
**URL:** `/get_files`  
**Method:** [`GET`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L150)  
**Description:** Retrieves a list of files available on the server.

**Expected JSON:**
```json
{
    "token": "string"
}
```

**Responses:**
- **200 OK:**
  ```json
  {
      "files": ["string"]
  }
  ```
- **400 Bad Request:**
  ```json
  {
      "message": "Invalid request"
  }
  ```
- **404 Not Found:**
  ```json
  {
      "message": "Peer not found"
  }
  ```

## Get a File
**URL:** `/get_file`  
**Method:** [`GET`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L188)  
**Description:** Retrieves the address of a file from the server.

**Expected JSON:**
```json
{
    "token": "string",
    "file_name": "string"
}
```

**Responses:**
- **200 OK:**
  ```json
  {
      "file_address": "string"
  }
  ```
- **400 Bad Request:**
  ```json
  {
      "message": "Invalid request"
  }
  ```
- **404 Not Found:**
  ```json
  {
      "message": "File not found"
  }
  ```
- **401 Unauthorized:**
  ```json
  {
      "message": "Peer not found"
  }
  ```

# Classes

## File
Represents a file in the system.
```python
class File:
    def __init__(self, filename: str, Peer: 'Peer') -> None:
        self.filename = filename
        self.Peer = Peer
    
    def __str__(self) -> str:
        return self.filename
```

## Peer
Represents a peer in the system.
```python
class Peer:
    def __init__(self, client_id: str, ip: str, port: int, token: str) -> None:
        self.ip = ip
        self.port = port
        self.client_id = client_id
        self.token = token
        
    def __iter__(self) -> iter:
        return iter(self.fileList)
```

## PeerHandler
Handles peer and file management.
```python
class PeerHandler:
    def __init__(self) -> None:
        self.peerList = []
        self.fileList = []
                
    def removePeerFiles(self, client_id: str) -> None:
        for file in self.fileList:
            if file.Peer.client_id == client_id:
                self.fileList.remove(file)
                       
    def addFile(self, filename: str, token: str) -> None:
        for peer in self.peerList:
            if peer.token == token:
                newFile = File(filename, peer)
                self.fileList.append(newFile)
    
    def addPeer(self, client_id: str, ip: str, port: int, token: str) -> None:
        newPeer = Peer(client_id, ip, port, token)
        self.peerList.append(newPeer)
        
    def removePeer(self, token: str) -> None:
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

    def getFileAddress(self, filename: str) -> str | None:
        for file in self.fileList:
            if file.filename == filename:
                return f"grpc://{file.Peer.ip}:{file.Peer.port}/{filename}"
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
```

## Config
Loads configuration from [`config.yaml`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/config.py).
```python
import yaml

class config:
    def __init__(self) -> None:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.token = config['auth']['token']
            self.control_port = config['control']['port']
            self.dataPort = config['peer']['port']
```