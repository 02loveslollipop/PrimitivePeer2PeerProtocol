from config import config
import requests
from flask import request, jsonify, Flask,session
from functools import wraps
import grpc
import p2p_pb2_grpc
import p2p_pb2
import datetime


'''
the peer server will listen to the config.dataPort port waiting for file request from other peers, when the process starts this peer must register in the master server and send it available files
'''

app = Flask(__name__)
config = config()
authHash = None

def registerInMaster(uri: str) -> None:
    '''
    Connects the peer to the master server and receives an authentication hash
    '''
    if authHash is not None:
        return
    
    global authHash
    with grpc.insecure_channel(f"{config.masterIP}:{config.masterPort}") as channel:
        stub = p2p_pb2_grpc.GreeterStub(channel)
        magicNumber = int(int(datetime.datetime.now(datetime.UTC).timestamp())/config.seed)
        authHash = str(stub.join(p2p_pb2.RegisterRequest(number=magicNumber, uri=uri)))

def unregisterInMaster() -> None:
    '''
    Disconnects the peer from the master server
    '''
    if authHash is None:
        return
    with grpc.insecure_channel(f"{config.masterIP}:{config.masterPort}") as channel:
        stub = p2p_pb2_grpc.GreeterStub(channel)
        response = stub.leave(p2p_pb2.RegisterRequest(hash=authHash))

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = p2p_pb2_grpc.GreeterStub(channel)
        

def checkIfAuthInMaster(Key: str):
    requests 
    


def authRequired(func):
    '''
    ## authRequired(func)
    Wrapper function for authentication, checks if the user is authenticated
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    app.run(debug=True,port=config.data_port)