# Tabla de Contenidos
1. [Editando Archivos de Configuración](#editando-archivos-de-configuración)
2. [Configuración del Servidor](#configuración-del-servidor)
3. [Configuración de Servidores Peer](#configuración-de-servidores-peer)
4. [Usando el Cliente Peer](#usando-el-cliente-peer)

# Editando Archivos de Configuración

### Configuración del Servidor
La configuración del servidor se almacena en `config.yaml`. Abre el archivo y edita los siguientes campos según sea necesario:
```yaml
control:
    port: 8000 # Puerto para escuchar mensajes de control entrantes
peer:
    port: 8001 # Puerto para escuchar datos entrantes o para solicitar datos
auth:
    token: "secret" # Token para autenticar
```

## Configuración del Peer
La configuración del peer también se almacena en `config.yaml`. Abre el archivo y edita los siguientes campos según sea necesario:
```yaml
ip: 107.23.96.211
port: 8000 # Puerto para escuchar mensajes de control entrantes
peer:
    port: 8001 # Puerto para escuchar datos entrantes o para solicitar datos
    path: "./files/" # Ruta del directorio para compartir
auth:
    token: "secret" # Token para autenticar
```

# Configuración del Servidor

1. **Instalar Dependencias**: Asegúrate de tener Python 3 instalado. Instala los paquetes requeridos usando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ejecutar el Servidor**: Navega al directorio del servidor y ejecuta el servidor:
     ```bash
     python3 server.py
     ```

# Configuración de Servidores Peer

1. **Instalar Dependencias**: Asegúrate de tener Python 3 instalado. Instala los paquetes requeridos usando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ejecutar el Servidor Peer**: Navega al directorio del peer y ejecuta el servidor peer:
     ```bash
     python3 peer.py --server
     ```

# Usando el Cliente Peer

1. **Instalar Dependencias**: Asegúrate de tener Python 3 instalado. Instala los paquetes requeridos usando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ejecutar el Cliente Peer**: Navega al directorio del peer y ejecuta el cliente peer:
     ```bash
     python3 peer.py
     ```

3. **Comandos CLI**:
     - **Ayuda**:
         ```bash
         help
         ```
     - **Conectar al Servidor**:
         ```bash
         connect [-h host] [-p port] [-t token]
         ```
         Si no se proporcionan host, puerto y token, se usarán los valores en el archivo de configuración.
     - **Desconectar del Servidor**:
         ```bash
         disconnect
         ```
     - **Listar Archivos**:
         ```bash
         list
         ```
     - **Obtener Dirección del Archivo**:
         ```bash
         where [-f file]
         ```
     - **Recuperar Archivo**:
         ```bash
         get [-f file] [-o output]
         ```
     - **Salir del Programa**:
         ```bash
         exit
         ```

## Ejemplo de Uso
1. **Conectar al Servidor**:
     ```bash
     connect
## Example Usage
1. **Connect to Server**:
   ```bash
   connect -h 127.0.0.1 -p 8000 -t secret
   ```

2. **List Files**:
   ```bash
   list
   ```

3. **Get File Address**:
   ```bash
   where -f example.txt
   ```

4. **Retrieve File**:
   ```bash
   get -f example.txt -o ./downloads/example.txt
   ```

5. **Disconnect from Server**:
   ```bash
   disconnect
   ```

6. **Exit Program**:
   ```bash
   exit
   ```
