# Echo server program
import socket
import sys

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 10000            # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
print 'socket now listening'
conn, addr = s.accept()

while 1:
	
	print 'Connected by', addr
	data = conn.recv(1024)
    #if not data: break
	conn.sendall(data)
conn.close()