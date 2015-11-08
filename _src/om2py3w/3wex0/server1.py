# -*- coding: utf-8 -*-
import socket
import sys
import jamesdiary

# 建立协议，当client发送信息为keyword时，返回所有日记历史信息
KEYWORD = 'P'

def response1(sock, data, address):
    """定义反应行为，如果接收到信息为KEYWORD，发回日记历史，否则则将信息记入日记"""
    if data == 'P':
        history_message = jamesdiary.readdiary()
        sent = sock.sendto(history_message, address)
        print >>sys.stderr, 'sent %s back to %s' % (sent, address)
 #   elif data=="q":
 #       sock.close()    
    else: 
        sent = sock.sendto(data, address)
        
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >>sys.stderr, data

        jamesdiary.writediary(data)
    



def main():
# Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    while True:
        print >>sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(4096)
        #print "py debug",len(data)
        if data == 'q':
            break
        response1(sock, data, address)

        #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        #print >>sys.stderr, data
    #if data:
        #sent = sock.sendto(data, address)
        #print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
    sock.close()


if __name__ == '__main__':
    main()



