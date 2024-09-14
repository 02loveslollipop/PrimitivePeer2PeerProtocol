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

def clear(stringBuffer: StringBuffer) -> None:
    stringBuffer.clear()
    stringBuffer += cu.init() + "\n"
    
def waitForInput(stringBuffer: StringBuffer) -> str:
    stringBuffer += cu.green(cu.prompt)
    print(stringBuffer, end='')
    result =  input()
    stringBuffer += result + "\n"
    return result

def listFiles(stringBuffer: StringBuffer) -> None:
    raise NotImplementedError("listFiles not implemented yet")\

def connect(stringBuffer: StringBuffer, host:str = None, port:int = None) -> None:
    raise NotImplementedError("connect not implemented yet")

def where(stringBuffer: StringBuffer, file:str) -> None:
    raise NotImplementedError("where not implemented yet")

def get(stringBuffer: StringBuffer, file:str) -> None:
    raise NotImplementedError("get not implemented yet")

def exit(stringBuffer: StringBuffer) -> None:
    stringBuffer += cu.red("Exiting the program\n")
    exit()

cli = False
isServerOn = False
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
            #Code of the server
            isServerOn = True
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
if not cli and not isServerOn:
    if path is None:
        path = conf.path
    peer = PeerServer(path)
    peer.run()
    
else:
    clearKey = 'cls' if os.name == 'nt' else 'clear'
    run = True
    stringBuffer = StringBuffer()
    clear(stringBuffer)
    while run:
        try:
            #clear the os screen
            os.system(clearKey)
            command = waitForInput(stringBuffer)
            '''
            # Command list
            - help: print the help message
            - connect [-h host] [-p port]: connect to the server, if no host AND port is given, the values in the configuration file will be used
            - list: list the files available in the server
            - where [-f file]: get the address of the file
            - get [-f file]: get the file
            - exit: exit the program
            '''
            if command == "help":
                stringBuffer += cu.help
            
        except KeyboardInterrupt:
            os.system(clearKey)
            exit()
        except Exception as e:
            error = str(e)
            stringBuffer += cu.red(f"\n{error}\n\n")
        
        
        
        
        
        
        
            
        