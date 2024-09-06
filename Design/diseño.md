# Red P2P
## Secuencia de comuniación
### Secuencia para mostrar disponibilidad y archivos disponibles
1. el peer envia mediante una llamada a una llamada gRPC al servidor un mensaje mostrando que esta disponible
2. el peer envia mediante un HTTP GET al servidor un JSON con la lista de manera jerarquica de los archivos que tiene disponibles, el servidor responde con un HTTP 200 mostrando que se recibio correctamente

### Secuencia para solicitar un archivo
1. el peer que requiere un archivo se comunica con el servidor mediante un HTTP GET solicitando la lista de archivos disponibles
2. el peer selecciona el archivo que desea y se comunica con el servidor mediante un HTTP GET solicitando la direccion del peer que tiene el archivo, el servidor responde con un HTTP 200 mostrando que se recibio correctamente
3. el peer se comunica con el peer que tiene el archivo mediante una llamdo HTTP GET solicitando el archivo, el peer que tiene el archivo responde con un HTTP 200 y envia el binario del archivo
4. el peer que solicito el archivo recibe el archivo en binario y lo guarda en su sistema de archivos
