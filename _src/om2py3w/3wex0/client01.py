# -*- coding: utf-8 -*-
# Echo client program
import socket
import sys


line1=""

HOST = 'localhost'    # The remote host
PORT = 10000            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

line1=raw_input("write:")
s.sendall(line1)


data = s.recv(1024)
s.close()
print 'Received', repr(data)