# Red P2P
## Secuencia de comuniación
### Secuencia para mostrar disponibilidad y archivos disponibles
1. el peer envia mediante una llamada a una llamada gRPC al servidor un mensaje mostrando que esta disponible
2. el peer envia mediante un HTTP GET al servidor un JSON con la lista de manera jerarquica de los archivos que tiene disponibles, el servidor responde con un HTTP 200 mostrando que se recibio correctamente

### Secuencia para solicitar un archivo
1. el peer que requiere un archivo se comunica con el servidor mediante un HTTP GET solicitando la lista de archivos disponibles
2. el peer selecciona el archivo que desea y se comunica con el servidor mediante un HTTP GET solicitando la direccion del peer que tiene el archivo y su hash de autenticacion, responde con un HTTP 200 con la direccion del archivo y el hash de autenticacion
3. el peer se comunica con el peer que tiene el archivo mediante una llamdo HTTP GET solicitando el archivo, el peer que tiene el archivo verifica en el servidor master si el usuario que esta solicitando el archivo esta autenticado, si lo esta responde con un HTTP 200 y envia el binario del archivo, si no responde con un HTTP 401

4. el peer que solicito el archivo recibe el archivo en binario y lo guarda en su sistema de archivos

### Secuencia de desconexión
1. el peer envia mediante una llamada a una llamada gRPC al servidor un mensaje mostrando que esta desconectado
2. el servidor elimina los archivos del peer de su lista de archivos disponibles

## Otras consideraciones
### Tiempo de vida
Si el proceso del peer se cierra de manera inesperada, no se ejecutaria la secuencia de desconexion, por lo que como medida extra se debe implementar un tiempo de vida para los peers, los peers deben enviar un mensaje de disponibilidad cada cierto tiempo, si el servidor no recibe un mensaje de disponibilidad en un tiempo determinado, se considera que el peer se desconecto y se eliminan los archivos del peer de la lista de archivos disponibles
