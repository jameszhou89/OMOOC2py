# -*- coding: utf-8 -*-
# Echo client program
import socket
import sys


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
#message = 'This is the message.  It will be repeated.'

message=''

while True:
  b_message = raw_input('>>> ')
  if b_message=="Y":
    a_message = raw_input('>>> ')
    message += a_message + '\n'

    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message,server_address)
    # Re sceive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data
  elif b_message=="N":
    break


sock.close()
