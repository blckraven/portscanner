import socket
from colorama import Fore

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input("[+] Enter Target IP: ")

def scanner(port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False

for portnum in range(1,65535):
    if scanner(portnum):
        if portnum == (20 or 21):
            print(Fore.GREEN + ("[*] Port", portnum, "/ftp", " is open"))
        elif portnum == 22:
            print(Fore.GREEN + ("[*] Port", portnum, "/ssh", " is open"))
        elif portnum == 23:
            print(Fore.GREEN + ("[*] Port", portnum,"/telnet", " is open"))
        elif portnum == 25:
            print(Fore.GREEN + ("[*] Port", portnum,"/smtp", " is open"))
        elif portnum == 53:
            print(Fore.GREEN + ("[*] Port", portnum,"/dns", " is open"))
        elif portnum == 67:
            print(Fore.GREEN + ("[*] Port", portnum,"/dhcp-server", " is open"))
        elif portnum == 68:
            print(Fore.GREEN + ("[*] Port", portnum,"/shcp-client", " is open"))
        elif portnum == 69:
            print(Fore.GREEN + ("[*] Port", portnum,"/tftp", " is open"))
        elif portnum == (80 or 8080):
            print(Fore.GREEN + ("[*] Port", portnum,"/http", " is open"))
        elif portnum == 110:
            print(Fore.GREEN + ("[*] Port", portnum,"/pop3", " is open"))
        elif portnum == 161:
            print(Fore.GREEN + ("[*] Port", portnum,"/snmp", " is open"))
        elif portnum == 443:
            print(Fore.GREEN + ("[*] Port", portnum,"/https", " is open"))
        elif portnum == 3306:
            print(Fore.GREEN + ("[*] Port", portnum,"/mysql", " is open"))
        else:
            print(Fore.GREEN + ("[*] Port", portnum," is open"))