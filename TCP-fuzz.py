import socket
from socket import error as SocketError

TCP_IP = "<IP>"
TCP_PORT = <PORT>

print("TCP target IP: %s" % TCP_IP)
print("TCP target port: %s" % TCP_PORT)

#LIST OF STRINGS TO SEND TO SERVER
input_file = open('list.txt', 'r')

for line in input_file:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    #CLIENT DISCONNECTS IF NO RESPONSE FOR 1 SECOND
    sock.settimeout(1.0)
    try:
        sock.sendall(str.encode(line))
        data = sock.recv(1024)
        print(line)
        print(data)
    #CATCHES SOCKET DISCONNECTION ERROR
    except SocketError as e:
        print(e)
        pass
