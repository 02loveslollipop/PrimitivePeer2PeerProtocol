import requests
import json
from config import config
#This script is used to test the /Server/Server.py API
#It sends a request to the server and check the response (if the response can be asserted, if not, it will print the response)

ip = "127.0.0.1"
port = 8000
conf = config()
token = None

#1. Test of /register endpoint
def test_register():
    global token
    url = f"http://{ip}:{port}/register"
    payload = {
        "client_id": "node_1",
        "ip": "192.168.1.1",
        "port": conf.dataPort,
        "genericToken": conf.token
    }

    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    token = str(response['token'])
    if type(response.get('token')) == str:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'token': 'string'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

#2. Test of /register endpoint when already registered
def test_register_already_registered():
    url = f"http://{ip}:{port}/register"
    payload = {
        "client_id": "node_1",
        "ip": "192.168.1.1",
        "port": conf.dataPort,
        "genericToken": conf.token
    }
    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Peer already registered'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Peer already registered'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 3. Test of /register endpoint with invalid token
def test_register_invalid_token():
    url = f"http://{ip}:{port}/register"
    payload = {
        "client_id": "node_2",
        "ip": "192.168.1.1",
        "port": conf.dataPort,
        "genericToken": "invalid_token"
    }
    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Invalid token'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid token'}
    else:
        print("\033[91m" + str(response) + "\033[0m")
        
# 4. Test of /add_file endpoint
def test_add_file():
    url = f"http://{ip}:{port}/add_file"
    payload = {
        "token": token,
        "file_name": "file1"
    }

    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'File added'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'File added'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 5. Test of /add_file endpoint with invalid token
def test_add_file_invalid_token():
    url = f"http://{ip}:{port}/add_file"
    payload = {
        "token": "invalid_token",
        "file_name": "file2"
    }
    
    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Peer not found'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid token'}
    else:
        print("\033[91m" + str(response) + "\033[0m")
    

# 6. Test of /add_file endpoint with invalid request
def test_add_file_invalid_request():
    url = f"http://{ip}:{port}/add_file"
    payload = {
        "token": token,
        "file_name": None
    }
    
    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Invalid request'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid request'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 7. Test of /get_files endpoint

def add_files_for_test_get_file_list():
    url = f"http://{ip}:{port}/add_file"
    payload = {
        "token": token,
        "file_name": "file2"
    }
    requests.post(url, json=payload)
    
    payload = {
        "token": token,
        "file_name": "file3"
    }
    requests.post(url, json=payload)
    
    payload = {
        "token": token,
        "file_name": "file4"
    }
    requests.post(url, json=payload)

def test_get_file_list():
    add_files_for_test_get_file_list()
    
    url = f"http://{ip}:{port}/get_files"
    payload = {
        "token": token
    }
    
    response = requests.get(url, json=payload)
    response = json.loads(response.text)
    if response == {'files': ['file1', 'file2', 'file3', 'file4']}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'fileList': ['file1', 'file2', 'file3', 'file4']}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 8. Test of /get_file_list endpoint with invalid token
def test_get_file_list_invalid_token():
    url = f"http://{ip}:{port}/get_files"
    payload = {
        "token": "invalid_token"
    }
    
    response = requests.get(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Peer not found'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid token'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 9. Test of /get_file_list endpoint with invalid request
def test_get_file_list_invalid_request():
    url = f"http://{ip}:{port}/get_files"
    payload = {
        "token": None
    }
    
    response = requests.get(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Invalid request'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid request'}
    else:
        print("\033[91m" + str(response) + "\033[0m")
    
# 10. Test of /get_file endpoint
def test_get_file():
    url = f"http://{ip}:{port}/get_file"
    payload = {
        "token": token,
        "file_name": "file1"
    }
    
    response = requests.get(url, json=payload)
    response = json.loads(response.text)
    print("\033[95m" + str(response) + "\033[0m")

# 11. Test of /get_file endpoint with invalid token
def test_get_file_invalid_token():
    url = f"http://{ip}:{port}/get_file"
    payload = {
        "token": "invalid_token",
        "file_name": "file1"
    }
    
    response = requests.get(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Peer not found'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid token'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 12. Test of /get_file endpoint with invalid request
def test_get_file_invalid_request():
    url = f"http://{ip}:{port}/get_file"
    payload = {
        "token": token,
        "file_name": None
    }

    response = requests.get(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Invalid request'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid request'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 13. Test of /unregister endpoint 
def test_unregister():
    url = f"http://{ip}:{port}/unregister"
    payload = {
        "token": token
    }
    
    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Peer unregistered'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Peer unregistered'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 14. Test of /unregister endpoint with invalid token
def test_unregister_invalid_token():
    url = f"http://{ip}:{port}/unregister"
    payload = {
        "token": "invalid_token"
    }
    
    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Peer not found'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid token'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

# 15. Test of /unregister endpoint with invalid request
def test_unregister_invalid_request():
    url = f"http://{ip}:{port}/unregister"
    payload = {
        "token": None
    }
    
    response = requests.post(url, json=payload)
    response = json.loads(response.text)
    if response == {'message': 'Invalid request'}:
        print("\033[92m" + str(response) + "\033[0m") # Expected output: {'message': 'Invalid request'}
    else:
        print("\033[91m" + str(response) + "\033[0m")

if __name__ == "__main__":
    
    # Modify the print statements to change the color in the terminal
    print("\033[96mTesting server API\033[0m")
    print("\033[93mTesting /register endpoint when not registered\033[0m")
    test_register()
    print("\033[93mTesting /register endpoint when already registered\033[0m")
    test_register_already_registered()
    print("\033[93mTesting /register endpoint with invalid token\033[0m")
    test_register_invalid_token()
    print("\033[93mTesting /add_file endpoint\033[0m")
    test_add_file()
    print("\033[93mTesting /add_file endpoint with invalid token\033[0m")
    test_add_file_invalid_token()
    print("\033[93mTesting /add_file endpoint with invalid request\033[0m")
    test_add_file_invalid_request()
    print("\033[93mTesting /get_files endpoint\033[0m")
    test_get_file_list()
    print("\033[93mTesting /get_files endpoint with invalid token\033[0m")
    test_get_file_list_invalid_token()
    print("\033[93mTesting /get_files endpoint with invalid request\033[0m")
    test_get_file_list_invalid_request()
    print("\033[93mTesting /get_file endpoint\033[0m")
    test_get_file()
    print("\033[93mTesting /get_file endpoint with invalid token\033[0m")
    test_get_file_invalid_token()
    print("\033[93mTesting /get_file endpoint with invalid request\033[0m")
    test_get_file_invalid_request()
    print("\033[93mTesting /unregister endpoint\033[0m")
    test_unregister()
    print("\033[93mTesting /unregister endpoint with invalid token\033[0m")
    test_unregister_invalid_token()
    print("\033[93mTesting /unregister endpoint with invalid request\033[0m")
    test_unregister_invalid_request()
