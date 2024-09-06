from config import config
import requests
from flask import request, jsonify, Flask,session
from functools import wraps

'''
the peer server will listen to the config.dataPort port waiting for file request from other peers, when the process starts this peer must register in the master server and send it available files
'''

app = Flask(__name__)
config = config()

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