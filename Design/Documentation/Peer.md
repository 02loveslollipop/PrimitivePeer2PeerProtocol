# Overview
The peer functionality in this P2P system includes the ability to connect to a server, list files, retrieve files, and manage peer connections. The main components are [`PeerClient`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/peerClient.py), [`PeerServer`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/peerServeer.py) and various utility functions.

# Configuration
The peer configuration is stored in [`config.yaml`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/config.yaml):
```yaml
ip: 107.23.96.211
port: 8000 # Port to listen for incoming control messages
peer:
  port: 8001 # Port to listen for incoming data or to request data
  path: "./files/" # Path of the directory to share
auth:
 

 token

: "secret" # Token to authenticate
```

# Classes

## PeerClient
Handles the client-side operations of a peer.

### Methods

- **`__init__(self, config: config) -> None`**
  - Initializes the client with the given configuration.
  - **Arguments:**
    - [`config`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/config.py): Configuration object containing network settings.
  - **Returns:** None

- **`register(self) -> None`**
  - Registers the peer with the server.
  - **Arguments:** None
  - **Returns:** None

- **`unregister(self) -> None`**
  - Unregisters the peer from the server.
  - **Arguments:** None
  - **Returns:** None

- **`getFileList(self) -> list[str]`**
  - Retrieves the list of files available on the server.
  - **Arguments:** None
  - **Returns:** List of file names.

- **`getFile(self, filename: str) -> str`**
  - Retrieves the address of a file from the server.
  - **Arguments:**
    - filename: Name of the file to retrieve.
  - **Returns:** File address as a string.

- **`getBinaryFile(self, filename: str) -> bytes`**
  - Retrieves the binary content of a file from the server.
  - **Arguments:**
    - filename: Name of the file to retrieve.
  - **Returns:** File content as bytes.

## PeerServer
Handles the server-side operations of a peer.

### Methods

- **`__init__(self, path: str, peer_config: config) -> None`**
  - Initializes the server with the given path and configuration.
  - **Arguments:**
    - path: Path to the directory where files are stored.
    - peer_config: Configuration object containing network settings.
  - **Returns:** None

- **`_addFile(token: str, filename: str, host: str, port: int) -> None`**
  - Adds a file to the server.
  - **Arguments:**
    - token: Name of the file to add.
    - host: Host of the server.
    - port: Port of the server.
  - **Returns:** None

- **`run(self) -> None`**
  - Runs the gRPC server.
  - **Arguments:** None
  - **Returns:** None

# Utility Functions

## Console Functions

- **`clear(stringBuffer: StringBuffer) -> None`**
  - Clears the string buffer and initializes it.
  - **Arguments:**
    - stringBuffer: The buffer to clear.
  - **Returns:** None

- **`waitForInput(stringBuffer: StringBuffer) -> str`**
  - Waits for user input and appends it to the buffer.
  - **Arguments:**
    - stringBuffer: The buffer to append input to.
  - **Returns:** User input as a string.

## Command Functions

- **`connect(stringBuffer: StringBuffer, peerClient: PeerClient, host: str = None, port: int = None, token: str = None) -> None`**
  - Connects to the server with optional host, port, and token.
  - **Arguments:**
    - stringBuffer: The buffer to append messages to.
    - peerClient: The peer client instance.
    - host: Optional host address.
    - port: Optional port number.
    - token: Optional authentication token.
  - **Returns:** None

- **`disconnect(stringBuffer: StringBuffer, peerClient: PeerClient) -> None`**
  - Disconnects from the server.
  - **Arguments:**
    - stringBuffer: The buffer to append messages to.
    - peerClient: The peer client instance.
  - **Returns:** None

- **`listFiles(stringBuffer: StringBuffer, peerClient: PeerClient) -> None`**
  - Lists the files available on the server.
  - **Arguments:**
    - stringBuffer: The buffer to append messages to.
    - peerClient: The peer client instance.
  - **Returns:** None

- **`where(stringBuffer: StringBuffer, peerClient: PeerClient, file: str) -> None`**
  - Retrieves the address of a file.
  - **Arguments:**
    - stringBuffer: The buffer to append messages to.
    - peerClient: The peer client instance.
    - file: Name of the file to locate.
  - **Returns:** None

- **`get(stringBuffer: StringBuffer, peerClient: PeerClient, file: str, output: str = None) -> None`**
  - Retrieves a file and saves it to the specified output path.
  - **Arguments:**
    - stringBuffer: The buffer to append messages to.
    - peerClient: The peer client instance.
    - file: Name of the file to retrieve.
    - output: Optional output path to save the file.
  - **Returns:** None

- **`exit(stringBuffer: StringBuffer) -> None`**
  - Exits the program.
  - **Arguments:**
    - stringBuffer: The buffer to append messages to.
  - **Returns:** None