# Echo server program
import socket
import sys

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 10000            # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


while 1:
	s.listen(10)
	print 'socket now listening'
	conn, addr = s.accept()
	print 'Connected by', addr
	data = conn.recv(1024)
    #if not data: break
	conn.sendall(data)
conn.close()


# -*- coding: utf-8 -*-
# Echo client program
import socket
import sys

line1=""


def writedairy():
	print "what do u want to say TODAY?"
	line1 = raw_input("line 1: ")
	return line1



HOST = 'localhost'    # The remote host
PORT = 10000            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


while True:
	line2 = raw_input("do u want to continue?if you want to continue print Y, want to quit print N ")
	if line2=="Y":
		line1=writedairy()
		s.sendall(line1)
		data = s.recv(1024) 
		print 'Received', repr(data)
		s.close()
	elif line2=="N":
		break
		print "And finally, we close it."

s.close()
