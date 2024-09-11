from config import config
from flask import Flask, request, jsonify
from peer import Peer
from file import File
from gRPCWorker import GRPCWorker
import grpc
import requests
from concurrent import futures

conf = config()
app = Flask(__name__)
peerList = []
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
gRPCWorker = GRPCWorker(server, conf.control_port, peerList, conf.ttl)

@app.route('/AddFile', methods=['POST'])
def addFile():
    """
    Peer adds a file to the network table
    """
    path = str(request.json['path'])
    for peer in peerList:
        peer = Peer(peer)
        if peer.isAvailable:
            peer.addFile(path)
            return jsonify({'status': 'File added successfully'})
    return jsonify({'status': 'No peer available to store the file'})

@app.route('/getFileTable', methods=['GET'])
def getFileTable():
    """
    Peer requests the file table
    """
    fileDirectory = {}
    for peer in peerList:
        peer = Peer(peer)
        for file in peer.fileList:
            fileDirectory[file.filename] = file.Peer.uri
    
    return jsonify({'fileDirectory': fileDirectory})

if __name__ == '__main__':
    print("hola")
    app.run(port=conf.control_port)
