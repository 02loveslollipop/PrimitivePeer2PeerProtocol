# Overview
Este servidor P2P permite a los peers registrarse, darse de baja y gestionar archivos. Utiliza Flask para el servidor web y soporta varios endpoints para la gestión de peers y archivos.

# Configuración
La configuración del servidor se almacena en [`config.yaml`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/config.yaml):
```yaml
port: 8000 # Puerto para escuchar mensajes de control entrantes
peer:
    port: 8001 # Puerto para escuchar datos entrantes o solicitar datos
auth:
    token: "secret" # Token para autenticar
```

# Endpoints

### Registrar un Peer
**URL:** `/register`  
**Método:** [`POST`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L20)  
**Descripción:** Registra un peer en el servidor y devuelve un token para futuras solicitudes.

**JSON Esperado:**
```json
{
        "client_id": "string",
        "ip": "string",
        "port": int,
        "genericToken": "string"
}
```

**Respuestas:**
- **200 OK:**
    ```json
    {
            "token": "string"
    }
    ```
- **400 Solicitud Incorrecta:**
    ```json
    {
            "message": "Peer already registered"
    }
    ```
- **401 No Autorizado:**
    ```json
    {
            "message": "Invalid token"
    }
    ```

## Dar de Baja un Peer
**URL:** `/unregister`  
**Método:** [`POST`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L69)  
**Descripción:** Da de baja un peer y elimina todos los archivos asociados.

**JSON Esperado:**
```json
{
        "token": "string"
}
```

**Respuestas:**
- **200 OK:**
    ```json
    {
            "message": "Peer unregistered"
    }
    ```
- **404 No Encontrado:**
    ```json
    {
            "message": "Invalid request"
    }
    ```
- **404 No Encontrado:**
    ```json
    {
            "message": "Peer not found"
    }
    ```

## Añadir un Archivo
**URL:** `/add_file`  
**Método:** [`POST`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L107)  
**Descripción:** Añade un archivo al servidor.

**JSON Esperado:**
```json
{
        "token": "string",
        "file_name": "string"
}
```

**Respuestas:**
- **200 OK:**
    ```json
    {
            "message": "File added"
    }
    ```
- **400 Solicitud Incorrecta:**
    ```json
    {
            "message": "Invalid request"
    }
    ```
- **404 No Encontrado:**
    ```json
    {
            "message": "Peer not found"
    }
    ```

## Obtener Archivos
**URL:** `/get_files`  
**Método:** [`GET`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L150)  
**Descripción:** Recupera una lista de archivos disponibles en el servidor.

**JSON Esperado:**
```json
{
        "token": "string"
}
```

**Respuestas:**
- **200 OK:**
    ```json
    {
            "files": ["string"]
    }
    ```
- **400 Solicitud Incorrecta:**
    ```json
    {
            "message": "Invalid request"
    }
    ```
- **404 No Encontrado:**
    ```json
    {
            "message": "Peer not found"
    }
    ```

## Obtener un Archivo
**URL:** `/get_file`  
**Método:** [`GET`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/server.py#L188)  
**Descripción:** Recupera la dirección de un archivo del servidor.

**JSON Esperado:**
```json
{
        "token": "string",
        "file_name": "string"
}
```

**Respuestas:**
- **200 OK:**
    ```json
    {
            "file_address": "string"
    }
    ```
- **400 Solicitud Incorrecta:**
    ```json
    {
            "message": "Invalid request"
    }
    ```
- **404 No Encontrado:**
    ```json
    {
            "message": "File not found"
    }
    ```
- **401 No Autorizado:**
    ```json
    {
            "message": "Peer not found"
    }
    ```

# Clases

## Archivo
Representa un archivo en el sistema.
```python
class File:
        def __init__(self, filename: str, Peer: 'Peer') -> None:
                self.filename = filename
                self.Peer = Peer
        
        def __str__(self) -> str:
                return self.filename
```

## Peer
Representa un peer en el sistema.
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

## Gestor de Peers
Gestiona la gestión de peers y archivos.
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

## Configuración
Carga la configuración desde [`config.yaml`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Server/config.py).
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