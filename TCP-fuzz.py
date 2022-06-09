import socket
from socket import error as SocketError

TCP_IP = "192.168.200.141"
TCP_PORT = 9876

print("TCP target IP: %s" % TCP_IP)
print("TCP target port: %s" % TCP_PORT)

input_file = open('list.txt', 'r')

for line in input_file:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    sock.settimeout(1.0)
    try:
        sock.sendall(str.encode(line))
        data = sock.recv(1024)
        print(line)
        print(data)
    except SocketError as e:
        print(e)
        pass
