from config import config
from flask import Flask, request, jsonify
from peerHandler import PeerHandler
from hashlib import sha256
import time

conf = config()
app = Flask(__name__)
peerHandler = PeerHandler()

def genAuthToken(client_id: str) -> str:
    input = client_id + str(time.time())
    return sha256(input.encode()).hexdigest()

def addPeer(client_id: str, ip: str, port: int) -> str:
    token = genAuthToken(client_id)
    peerHandler.addPeer(client_id, ip, port, token)
    return token

@app.route('/register', methods=['POST'])
def register():
    '''
    # Register a peer Endpoint
    register a peer in the server and return a token to the peer to store and use in future requests
    ## Expected JSON
        {
            "client_id": "string",
            "ip": "string",
            "port": int
            "genericToken": "string"
        }
    ## Return if successful  
        {
            "token": "string"
        }
        http status code 200
    ## Return if invalid request
        {
            "message": "Peer already registered"
        }
        http status code 400  
    ## Return if invalid token
        {
            "message": "Invalid token"
        }
        http status code 401
    
    '''
    try:
        client_id = request.json['client_id']
        ip = request.json['ip']
        port = request.json['port']
        genericToken = request.json['genericToken']
    except KeyError:
        return jsonify({"message": "Invalid request"}), 400
    
    if client_id is None or ip is None or port is None or genericToken is None:
        return jsonify({"message": "Invalid request"}), 400
    
    if genericToken != conf.token:
        return jsonify({"message": "Invalid token"}), 401
    
    if peerHandler.peerExists(client_id):
        return jsonify({"message": "Peer already registered"}), 400

    token = addPeer(client_id, ip, port)
    return jsonify({"token": token}), 200

@app.route('/unregister', methods=['POST'])
def unregister():
    '''
    # Unregister a peer Endpoint
    unregister a peer in the server and remove all files associated with the peer
    ## Expected JSON
        {
            "token": "string"
        }
    ## Return if successful  
        {
            "message": "Peer unregistered"
        }
        http status code 200
    ## Return if invalid request
        {
            "message": "Invalid request"
        }
        http status code 404
    ## Return if peer not registered
        {
            "message": "Peer not found"
        }
    '''
    try:
        token = request.json['token']
    except KeyError:
        return jsonify({"message": "Invalid request"}), 400

    if token is None:
        return jsonify({"message": "Invalid request"}), 400
    
    if not peerHandler.authPeer(token):
        return jsonify({"message": "Peer not found"}), 404
    
    peerHandler.removePeer(token)
    return jsonify({"message": "Peer unregistered"}), 200

@app.route('/add_file', methods=['POST'])
def add_file():
    '''
    

    # Add file Endpoint
    add a file to the server
    ## Expected JSON
        {
            "token": "string",
            "file_name": "string"
        }
    ## Return if successful  
        {
            "message": "File added"
        }
        http status code 200
    ## Return if invalid request
        {
            "message": "Invalid request"
        }
        http status code 400
    ## Return if peer not found
        {
            "message": "Peer not found"
        }
        http status code 404
    '''
    try:
        token = request.json['token']
        file_name = request.json['file_name']
    except KeyError:
        return jsonify({"message": "Invalid request"}), 400
    
    if token is None or file_name is None:
        return jsonify({"message": "Invalid request"}), 400
    
    if not peerHandler.authPeer(token):
        return jsonify({"message": "Peer not found"}), 404
    
    peerHandler.addFile(file_name, token)
    return jsonify({"message": "File added"}), 200

@app.route('/get_files', methods=['GET']) #TODO: check if this should be a POST request
def get_files(): 
    '''
    # Get files Endpoint
    get a list of files available in the server
    ## Expected JSON
        {
            "token": "string"
        }
    ## Return if successful  
        {
            "files": ["string"]
        }
        http status code 200
    ## Return if invalid request
        {
            "message": "Invalid request"
        }
        http status code 400
    ## Return if peer not found
        {
            "message": "Peer not found"
        }
        http status code 404
    '''
    try:
        token = request.json['token']
    except KeyError:
        return jsonify({"message": "Invalid request"}), 400
    
    if token is None:
        return jsonify({"message": "Invalid request"}), 400
    
    if not peerHandler.authPeer(token):
        return jsonify({"message": "Peer not found"}), 404
    
    return jsonify({"files": peerHandler.getFileList()}), 200

@app.route('/get_file', methods=['GET'])
def get_file():
    '''
    # Get file Endpoint
    get a file from the server
    ## Expected JSON
        {
            "token": "string",
            "file_name": "string"
        }
    ## Return if successful  
        {
            "file_address": "string"
        }
        http status code 200
    ## Return if invalid request
        {
            "message": "Invalid request"
        }
        http status code 400
    ## Return if file not found
        {
            "message": "File not found"
        }
        http status code 404
    ## Return if peer not found
        {
            "message": "Peer not found"
        }
        http status code 404
    '''
    try:
        token = request.json['token']
        file_name = request.json['file_name']
    except KeyError:
        return jsonify({"message": "Invalid request"}), 400
    
    if token is None or file_name is None:
        return jsonify({"message": "Invalid request"}), 400
    
    if not peerHandler.authPeer(token):
        return jsonify({"message": "Peer not found"}), 401
    
    file_address = peerHandler.getFileAddress(file_name)
    
    if file_address is None:
        return jsonify({"message": "File not found"}), 404

    return jsonify({"file_address": file_address}), 200

if __name__ == '__main__':
    app.run(port=conf.control_port, debug=True)

        

        
    

