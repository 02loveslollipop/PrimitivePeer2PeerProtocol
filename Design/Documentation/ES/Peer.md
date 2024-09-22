# Overview
La funcionalidad de los peers en este sistema P2P incluye la capacidad de conectarse a un servidor, listar archivos, recuperar archivos y gestionar conexiones entre peers. Los componentes principales son [`PeerClient`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/peerClient.py), [`PeerServer`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/peerServeer.py) y varias funciones utilitarias.

# Configuración
La configuración del peer se almacena en [`config.yaml`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/config.yaml):
```yaml
ip: 107.23.96.211
port: 8000 # Puerto para escuchar mensajes de control entrantes
peer:
    port: 8001 # Puerto para escuchar datos entrantes o solicitar datos
    path: "./files/" # Ruta del directorio para compartir
auth:
    token: "secret" # Token para autenticar
```

# Clases

## PeerClient
Maneja las operaciones del lado del cliente de un peer.

### Métodos

- **`__init__(self, config: config) -> None`**
    - Inicializa el cliente con la configuración dada.
    - **Argumentos:**
        - [`config`](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/blob/main/Peer/config.py): Objeto de configuración que contiene los ajustes de red.
    - **Retorna:** Ninguno

- **`register(self) -> None`**
    - Registra el peer con el servidor.
    - **Argumentos:** Ninguno
    - **Retorna:** Ninguno

- **`unregister(self) -> None`**
    - Desregistra el peer del servidor.
    - **Argumentos:** Ninguno
    - **Retorna:** Ninguno

- **`getFileList(self) -> list[str]`**
    - Recupera la lista de archivos disponibles en el servidor.
    - **Argumentos:** Ninguno
    - **Retorna:** Lista de nombres de archivos.

- **`getFile(self, filename: str) -> str`**
    - Recupera la dirección de un archivo del servidor.
    - **Argumentos:**
        - filename: Nombre del archivo a recuperar.
    - **Retorna:** Dirección del archivo como una cadena.

- **`getBinaryFile(self, filename: str) -> bytes`**
    - Recupera el contenido binario de un archivo del servidor.
    - **Argumentos:**
        - filename: Nombre del archivo a recuperar.
    - **Retorna:** Contenido del archivo en bytes.

## PeerServer
Maneja las operaciones del lado del servidor de un peer.

### Métodos

- **`__init__(self, path: str, peer_config: config) -> None`**
    - Inicializa el servidor con la ruta y configuración dadas.
    - **Argumentos:**
        - path: Ruta al directorio donde se almacenan los archivos.
        - peer_config: Objeto de configuración que contiene los ajustes de red.
    - **Retorna:** Ninguno

- **`_addFile(token: str, filename: str, host: str, port: int) -> None`**
    - Agrega un archivo al servidor.
    - **Argumentos:**
        - token: Nombre del archivo a agregar.
        - host: Host del servidor.
        - port: Puerto del servidor.
    - **Retorna:** Ninguno

- **`run(self) -> None`**
    - Ejecuta el servidor gRPC.
    - **Argumentos:** Ninguno
    - **Retorna:** Ninguno

# Funciones Utilitarias

## Funciones de Consola

- **`clear(stringBuffer: StringBuffer) -> None`**
    - Limpia el buffer de cadenas y lo inicializa.
    - **Argumentos:**
        - stringBuffer: El buffer a limpiar.
    - **Retorna:** Ninguno

- **`waitForInput(stringBuffer: StringBuffer) -> str`**
    - Espera la entrada del usuario y la agrega al buffer.
    - **Argumentos:**
        - stringBuffer: El buffer al que agregar la entrada.
    - **Retorna:** Entrada del usuario como una cadena.

## Funciones de Comando

- **`connect(stringBuffer: StringBuffer, peerClient: PeerClient, host: str = None, port: int = None, token: str = None) -> None`**
    - Conecta al servidor con host, puerto y token opcionales.
    - **Argumentos:**
        - stringBuffer: El buffer al que agregar mensajes.
        - peerClient: La instancia del cliente peer.
        - host: Dirección del host opcional.
        - port: Número de puerto opcional.
        - token: Token de autenticación opcional.
    - **Retorna:** Ninguno

- **`disconnect(stringBuffer: StringBuffer, peerClient: PeerClient) -> None`**
    - Desconecta del servidor.
    - **Argumentos:**
        - stringBuffer: El buffer al que agregar mensajes.
        - peerClient: La instancia del cliente peer.
    - **Retorna:** Ninguno

- **`listFiles(stringBuffer: StringBuffer, peerClient: PeerClient) -> None`**
    - Lista los archivos disponibles en el servidor.
    - **Argumentos:**
        - stringBuffer: El buffer al que agregar mensajes.
        - peerClient: La instancia del cliente peer.
    - **Retorna:** Ninguno

- **`where(stringBuffer: StringBuffer, peerClient: PeerClient, file: str) -> None`**
    - Recupera la dirección de un archivo.
    - **Argumentos:**
        - stringBuffer: El buffer al que agregar mensajes.
        - peerClient: La instancia del cliente peer.
        - file: Nombre del archivo a localizar.
    - **Retorna:** Ninguno

- **`get(stringBuffer: StringBuffer, peerClient: PeerClient, file: str, output: str = None) -> None`**
    - Recupera un archivo y lo guarda en la ruta de salida especificada.
    - **Argumentos:**
        - stringBuffer: El buffer al que agregar mensajes.
        - peerClient: La instancia del cliente peer.
        - file: Nombre del archivo a recuperar.
        - output: Ruta de salida opcional para guardar el archivo.
    - **Retorna:** Ninguno

- **`exit(stringBuffer: StringBuffer) -> None`**
    - Sale del programa.
    - **Argumentos:**
        - stringBuffer: El buffer al que agregar mensajes.
    - **Retorna:** Ninguno
