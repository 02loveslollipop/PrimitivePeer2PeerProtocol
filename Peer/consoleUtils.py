import datetime
import os
import socket

def black(text: str) -> str:
    return "\033[30m" + text + "\033[0m"

def red(text: str) -> str:
    return "\033[31m" + text + "\033[0m"

def green(text: str) -> str:
    return "\033[32m" + text + "\033[0m"

def yellow(text: str) -> str:
    return "\033[33m" + text + "\033[0m"

def blue(text: str) -> str:
    return "\033[34m" + text + "\033[0m"

def magenta(text: str) -> str:
    return "\033[35m" + text + "\033[0m"

def cyan(text: str) -> str:
    return "\033[36m" + text + "\033[0m"

def white(text: str) -> str:
    return "\033[37m" + text + "\033[0m"

def reset(text: str) -> str:
    return "\033[0m" + text + "\033[0m"

def bold(text: str) -> str:
    return "\033[1m" + text + "\033[0m"

def underline(text: str) -> str:
    return "\033[4m" + text + "\033[0m"

def init():
    time = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    osName = os.uname().sysname
    architechture = os.uname().machine
    return f"{yellow(bold(f'Primitive Peer 2 Peer Protocol (P4) [{time}] ({osName}, {architechture})'))}.\n\n{host} at {ip}.\nType 'help' for more information.\n"

def helpHandler():
    string = "Welcome to the Primitive Peer 2 Peer Protocol (P4) console line interface help utility! If this is your first time using this program, you should read the documentation.\n\n"
    string += blue(bold("The command of the utility are:\n\n"))
    string += "- help: print the help message\n"
    string += f"- connect {yellow('[-h host]')} {yellow('[-p port]')}: connect to the server, if no host AND port is given, the values in the configuration file will be used\n"
    string += f"- list: list the files available in the server\n"
    string += f"- where {yellow('[-f file]')}: get the address of the file\n"
    string += f"- get {yellow('[-f file]')}: get the file\n"
    string += f"- exit: exit the program\n"
    return string

help = helpHandler()
prompt = green("P4> ")


        
__package__ = "consoleUtils"



