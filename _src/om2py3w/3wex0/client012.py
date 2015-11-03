# -*- coding: utf-8 -*-
# Echo client program
import socket
import sys

line1=""


def writedairy():
	print "what do u want to say TODAY?"
	line2 = raw_input("line 1: ")
	return line2



HOST = 'localhost'    # The remote host
PORT = 10000            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


while True:
	line2 = raw_input("do u want to continue?if you want to continue print Y, want to quit print N ")
	if line2=="Y":
		writedairy()
		s.sendall(line2)
		data = s.recv(1024)
	elif line2=="N":
		break
		print "And finally, we close it."

s.close()
print 'Received', repr(data)