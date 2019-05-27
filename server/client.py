#client example
import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))


msg=input('tki ?')
client_socket.send(msg.encode())

while 1:
    data = client_socket.recv(512)
    if ( data == 'q' or data == 'Q'):
        client_socket.close()
        break;
    else:
        print("RECIEVED:" + str(data))
