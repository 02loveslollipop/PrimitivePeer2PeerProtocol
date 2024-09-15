from peerClient import PeerClient
from peerServer import PeerServer
from config import config
import os
import sys
import consoleUtils as cu

class StringBuffer:
    def __init__(self):
        self.buffer = ""
        
    def __iadd__(self, other) -> None:
        if type(other) == str:
            self.buffer += other
            return self
        else:
            try:
                self.buffer += str(other)
                return self
            except:
                self.buffer += "{could not convert object to string}"
                return self
    
    def __str__(self) -> str:
        return self.buffer

    def clear(self):
        self.buffer = ""
    
    def get(self) -> str:
        return self.buffer

# Console functions
def clear(stringBuffer: StringBuffer) -> None:
    stringBuffer.clear()
    stringBuffer += cu.init() + "\n"
    
def waitForInput(stringBuffer: StringBuffer) -> str:
    stringBuffer += cu.green(cu.prompt)
    print(stringBuffer, end='')
    result =  input()
    stringBuffer += result + "\n"
    return result

# Command functions
def connect(stringBuffer: StringBuffer, peerClient: PeerClient, host:str = None, port:int = None, token:str = None) -> None:
    if host is not None:
        peerClient.config.ip = host
    if port is not None:
        peerClient.config.control_port = port
    if token is not None:
        peerClient.config.token = token
    peerClient.register()
    stringBuffer += cu.cyan(f"Connected to {peerClient.config.ip}:{peerClient.config.control_port}\n")

def disconnect(stringBuffer: StringBuffer, peerClient: PeerClient) -> None:
    peerClient.unregister()
    stringBuffer += cu.cyan("Disconnected from the server\n")

def listFiles(stringBuffer: StringBuffer, peerClient: PeerClient) -> None:
    files = peerClient.getFileList()
    stringBuffer += cu.cyan(f"files@{peerClient.config.ip}:{peerClient.config.control_port}\n")
    if len(files) == 0:
        stringBuffer += "*\n"
        return
    for file in files:
        stringBuffer += f"{file}\n"


def where(stringBuffer: StringBuffer, peerClient: PeerClient, file:str) -> None:
    address = peerClient.getFile(file)
    stringBuffer += cu.magenta(f"{file} is available at {address}\n")


def get(stringBuffer: StringBuffer, peerClient: PeerClient, file:str, output:str = None) -> None:
    if output is None:
        output = os.path.join(os.getcwd(), file)
    url = peerClient.getFile(file, output)
    msg = f"{file} found at {url}"
    print(msg, end="\n")
    stringBuffer += cu.cyan(msg) + "\n"
    msg = cu.cyan(f"Retrieving {file}...")
    print(msg, end="\n")
    stringBuffer += msg + "\n"
    bytesArray = peerClient.getBinaryFile(file)
    print(bytesArray) #TODO: remove this line
    msg = cu.cyan(f"Saving {file} to {output}")
    print(msg, end="\n")
    stringBuffer += msg + "\n"
    with open(output, "wb") as f:
        f.write(bytesArray)
    

def exit(stringBuffer: StringBuffer) -> None:
    stringBuffer += cu.red("Exiting the program\n")
    sys.exit(0)

# initialization
cli = False
deprecateNextArg = False
path = None

args = os.sys.argv
if len(args) == 1:
    print("No argument given, running the interactive CLI")
    cli = True 
else:
    for i in range(len(args)):
        if deprecateNextArg:
            deprecateNextArg = False
            break
        elif args[i] == "--server":
            cli = False

            break
        elif args[i] == "--configPath":
            path = args[i+1]
            deprecateNextArg = True
            break
        elif args[i] == "--help":
            print("Usage: python3 peer.py [--server] [--configPath path] [--help]")
            print("--server: run the server")
            print("--configPath: the path to the configuration file")
            print("--help: print this message")
            print("If no argument is given, the program will run the interactive CLI")
            break
        elif args[i].startswith("--"):
            print(f"{args[i]} has not been recognized as a valid argument")
            break

#if debug path is an absolute path

gettrace = getattr(sys, 'gettrace', None)

if gettrace is None:
    print('No sys.gettrace')
elif gettrace():
    print('Running in debug mode, path set to an arbitrary absolute path')
    path = "/home/zerotwo/p2pFileShare/Peer/config.yaml"

conf = config(path)

# Server mode
if not cli:
    if path is None:
        path = conf.path
    peer = PeerServer(path, conf)
    peer.run()

# Client mode    
else:
    clearKey = 'cls' if os.name == 'nt' else 'clear'
    run = True
    stringBuffer = StringBuffer()
    peerClient = PeerClient(conf)
    connected = False
    clear(stringBuffer)
    while run:
        try:
            #clear the os screen
            os.system(clearKey)
            command = waitForInput(stringBuffer)
            '''
            # Command list
            - help: print the help message
            - connect [-h host] [-p port] [-t token]: connect to the server, if no host AND port is given, the values in the configuration file will be used
            - disconnect: disconnect from the server
            - list: list the files available in the server
            - where [-f file]: get the address of the file
            - get [-f file] [-o output]: get the file and save it in the output file
            - exit: exit the program
            '''
            # help command
            if command == "help": 
                stringBuffer += cu.help
                
            # connect command
            elif command.startswith("connect"):
                if len(command) == 7:
                    connect(stringBuffer, peerClient)
                else:
                    host = None
                    port = None
                    token = None
                    skipNext = False
                    command = command.split(" ")
                    for i in range(len(command)):
                        if skipNext:
                            skipNext = False
                            continue
                        elif command[i] == "-h":
                            host = command[i+1]
                        elif command[i] == "-p":
                            port = int(command[i+1])
                        elif command[i] == "-t":
                            token = command[i+1]
                        else:
                            stringBuffer += cu.red("Invalid arguments. For more information, type 'help'\n")
                            break
                    connect(stringBuffer, peerClient, host, port, token)
                connected = True
                    
            # disconnect command      
            elif command == "disconnect":
                disconnect(stringBuffer, peerClient)
                connected = False
            
            # list command
            elif command == "list":
                if not connected:
                    stringBuffer += cu.red("You are not connected to the server. For more information, type 'help'\n")
                else:
                    listFiles(stringBuffer, peerClient)
                    
            # where command
            elif command.startswith("where"):
                if not connected:
                    stringBuffer += cu.red("You are not connected to the server. For more information, type 'help'\n")
                else:
                    command = command.split(" ")
                    if len(command) == 1 or len(command) > 3:
                        stringBuffer += cu.red("Invalid arguments. For more information, type 'help'\n")
                    else:
                        where(stringBuffer, peerClient, command[1])
                        
            # get command
            elif command.startswith("get"):
                if not connected:
                    stringBuffer += cu.red("You are not connected to the server. For more information, type 'help'\n")
                else:
                    command = command.split(" ")
                    if len(command) == 5:
                        if command[1] == "-f" and command[3] == "-o":
                            file = command[2]
                            output = command[4]
                            get(stringBuffer, peerClient, file, output)
                        elif command[1] == "-o" and command[3] == "-f":
                            file = command[4]
                            output = command[2]
                            get(stringBuffer, peerClient, file, output)
                        else:
                            stringBuffer += cu.red("Invalid arguments. For more information, type 'help'\n")
                    if len(command) == 3:
                        if command[1] == "-f":
                            file = command[2]
                            get(stringBuffer, peerClient, file)
                        else:
                            stringBuffer += cu.red("Invalid arguments. For more information, type 'help'\n")
                    else:
                        stringBuffer += cu.red("Invalid arguments. For more information, type 'help'\n")
            
            # exit command
            elif command == "exit":
                exit(stringBuffer)
            
            # invalid command
            else:
                stringBuffer += cu.red("Invalid command. For more information, type 'help'\n")

        except KeyboardInterrupt:
            os.system(clearKey)
            exit(stringBuffer)
        except Exception as e:
            error = str(e)
            stringBuffer += cu.red(f"\n{error}\n\n")
        
        
        
        
        
        
        
            
        