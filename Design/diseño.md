# Primitive Peer 2 Peer Protocol (P4)
## EN
### Channels
#### Control channel
A REST API will be used for the control channel, the master server and the peers will communicate via HTTP, the master server will have an open port to receive requests from the peers, the peers will communicate with the master server to show their availability, request the list of available files and request the address of a specific file
#### Data channel
gRPC will be used for the data channel, the peers will communicate with each other via gRPC to send and receive files
### Communication sequence
#### Sequence to show availability and available files
1. the peer sends an HTTP POST to the server a message showing that it is available, the server returns an authentication token
2. the peer sends an HTTP POST to the server a JSON with the list of files that it has available in a hierarchical way, the server responds with an HTTP 200 showing that it was received correctly
### Sequence to request a file
1. the peer that requires a file communicates with the server via an HTTP POST requesting the list of available files
2. the peer selects the file it wants and communicates with the server via an HTTP POST requesting the address of the peer that has the file, responds with an HTTP 200 with the address of the file
3. the peer communicates with the peer that has the file via a gRPC call requesting the file, the peer that has the file verifies in the master server if the user requesting the file is authenticated, if it is, it responds with an HTTP 200 and sends the binary of the file, if not, it responds with an HTTP 401
4. the peer that requested the file receives the file in binary and saves it in its file system
#### Disconnection sequence
1. the peer sends a message showing that it is disconnected via an HTTP POST call to the server
2. the server removes the peer's files from its list of available files
### Other considerations (not implemented)
#### TTL (Time to live)
If the peer process closes unexpectedly, the disconnection sequence would not be executed, so as an extra measure, a time to live must be implemented for the peers, the peers must send a message of availability every certain time, if the server does not receive a message of availability in a certain time, it is considered that the peer disconnected and the peer's files are removed from the list of available files

## ES
## Canales
### Canal de control
Se usara una API REST para el canal de control, el servidor master y los peers se comunicaran mediante HTTP, el servidor master tendra un puerto abierto para recibir las peticiones de los peers, los peers se comunicaran con el servidor master para mostrar su disponibilidad, solicitar la lista de archivos disponibles y solicitar la direccion de un archivo en especifico
### Canal de datos
Se usara gRPC para el canal de datos, los peers se comunicaran entre si mediante gRPC para enviar y recibir archivos
## Secuencia de comuniación
### Secuencia para mostrar disponibilidad y archivos disponibles
1. el peer envia mediante un HTTP POST al servidor un mensaje mostrando que esta disponible, el servidor restorna una token  de autenticacion
2. el peer envia mediante un HTTP POST al servidor un JSON con la lista de manera jerarquica de los archivos que tiene disponibles, el servidor responde con un HTTP 200 mostrando que se recibio correctamente

### Secuencia para solicitar un archivo
1. el peer que requiere un archivo se comunica con el servidor mediante un HTTP POST solicitando la lista de archivos disponibles
2. el peer selecciona el archivo que desea y se comunica con el servidor mediante un HTTP POST solicitando la direccion del peer que tiene el archivo, responde con un HTTP 200 con la direccion del archivo
3. el peer se comunica con el peer que tiene el archivo mediante una llamdo gRPC solicitando el archivo, el peer que tiene el archivo verifica en el servidor master si el usuario que esta solicitando el archivo esta autenticado, si lo esta responde con un HTTP 200 y envia el binario del archivo, si no responde con un HTTP 401

4. el peer que solicito el archivo recibe el archivo en binario y lo guarda en su sistema de archivos

### Secuencia de desconexión
1. el peer envia mediante una llamada a un HTTP POST al servidor un mensaje mostrando que esta desconectado
2. el servidor elimina los archivos del peer de su lista de archivos disponibles

## Otras consideraciones (no implementadas)
### Tiempo de vida
Si el proceso del peer se cierra de manera inesperada, no se ejecutaria la secuencia de desconexion, por lo que como medida extra se debe implementar un tiempo de vida para los peers, los peers deben enviar un mensaje de disponibilidad cada cierto tiempo, si el servidor no recibe un mensaje de disponibilidad en un tiempo determinado, se considera que el peer se desconecto y se eliminan los archivos del peer de la lista de archivos disponibles

