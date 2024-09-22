# Table of Contents
1. [Editing Configuration Files](#editing-configuration-files)
2. [Setting Up the Server](#setting-up-the-server)
3. [Setting Up Peer Servers](#setting-up-peer-servers)
4. [Using the Peer Client](#using-the-peer-client)

# Editing Configuration Files

### Server Configuration
The server configuration is stored in `config.yaml`. Open the file and edit the following fields as needed:
```yaml
control:
  port: 8000 # Port to listen for incoming control messages
peer:
  port: 8001 # Port to listen for incoming data to

 request

 data
auth:
  token: "secret" # Token to authenticate
```

## Peer Configuration
The peer configuration is also stored in `config.yaml`. Open the file and edit the following fields as needed:
```yaml
ip: 107.23.96.211
port: 8000 # Port to listen for incoming control messages
peer:
  port: 8001 # Port to listen for incoming data or to request data
  path: "./files/" # Path of the directory to share
auth:
  token: "secret" # Token to authenticate
```

# Setting Up the Server

1. **Install Dependencies**: Ensure you have Python 3 installed. Install required packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server**: Navigate to the server directory and run the server:
   ```bash
   python3 server.py
   ```

# Setting Up Peer Servers

1. **Install Dependencies**: Ensure you have Python 3 installed. Install required packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Peer Server**: Navigate to the peer directory and run the peer server:
   ```bash
   python3 peer.py --server
   ```

# Using the Peer Client

1. **Install Dependencies**: Ensure you have Python 3 installed. Install required packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Peer Client**: Navigate to the peer directory and run the peer client:
   ```bash
   python3 peer.py
   ```

3. **CLI Commands**:
   - **Help**:
     ```bash
     help
     ```
   - **Connect to Server**:
     ```bash
     connect [-h host] [-p port] [-t token]
     ```
     If no host, port, and token are given, the values in the configuration file will be used.
   - **Disconnect from Server**:
     ```bash
     disconnect
     ```
   - **List Files**:
     ```bash
     list
     ```
   - **Get File Address**:
     ```bash
     where [-f file]
     ```
   - **Retrieve File**:
     ```bash
     get [-f file] [-o output]
     ```
   - **Exit Program**:
     ```bash
     exit
     ```

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
