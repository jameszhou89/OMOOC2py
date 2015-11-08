# -*- coding: utf-8 -*-
# Echo client program
import socket
import sys

#建立协议，当client发送信息为keyword时，返回所有日记历史信息
KEYWORD = 'P'

def main():
# Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 10000)
#message = 'This is the message.  It will be repeated.'

    sock.sendto(KEYWORD,server_address)
    data, server = sock.recvfrom(4096)
    print data

    message=''

    while True:
        b_message = raw_input('"if you want to continue print Y, want to quit print N " ')
        if b_message=="Y":
            a_message = raw_input('>>> ')
            message = a_message

            print >>sys.stderr, 'sending "%s"' % message
            sent = sock.sendto(message,server_address)

            if message=="q":
              break

    #如何保存数据？


    # Receive response
            print >>sys.stderr, 'waiting to receive'
            data, server = sock.recvfrom(4096)
            print >>sys.stderr, 'received "%s"' % data

        elif b_message=="N":
            break
    sock.close()


if __name__ == '__main__':
    main()