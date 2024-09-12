from flask import jsonify, Flask, request

app = Flask(__name__)
user_list = []
file_list = []
tokenAuth = "1234"

def genAuthToken(client_id: str) -> str:
    # TODO: Implement this function, it should generate a unique token to be used for authentication by the peer
    return "1234"

def removePeerFiles(client_id: str) -> None:
    #TODO: Implement this function, it should remove all files associated with the peer given as argument
    pass

def addUser(client_id: str, ip: str, token: str) -> None:
    #TODO: Implement this function, it should add a user to the user_list
    pass

def removeUser(token: str) -> None:
    #TODO: Implement this function, it should remove a user from the user_list
    pass

def AuthToken(token: str) -> bool:
    #TODO: Implement this function, it should check if the token is valid
    return True


@app.route('/login', methods=['POST'])
def login():
    #get the username and password from the request json
    token = request.json.get('token')
    client_id = request.json.get('client_id')
    ip = request.json.get('ip')
    if token is None or client_id is None:
        return jsonify({'error': 'Missing token or client_id'}), 400

    if token == tokenAuth:
        return jsonify({'error': 'Token already exists'}),
    
    token = genAuthToken(client_id)
    addUser(client_id, ip, token)

@app.route('/logout', methods=['POST'])
def logout():
    token = request.json.get('token')
    if token is None:
        return jsonify({'error': 'Missing token'}), 400
    for user in user_list: #TODO: change user_list to userClass
        if user['token'] == token:
            removeUser(token)
            removePeerFiles(user['client_id'])
            return jsonify({'message': 'User logged out successfully'})
    return jsonify({'error': 'User not found'}), 404

@app.route('/add_file', methods=['POST'])
def add_file():
    token = request.json.get('token')
    file_name = request.json.get('file_name')
    if token is None or file_name is None:
        return jsonify({'error': 'Missing token or file_name'}), 400
    for user in user_list: #TODO: change user_list to userClass
        if user['token'] == token:

@app.route('/get_files', methods=['GET'])
def get_files():
    token = request.json.get('token')
    if token is None:
        return jsonify({'error': 'Missing token'}), 400
    for user in user_list:
        if user['token'] == token:
            return jsonify({'files': file_list})


        



