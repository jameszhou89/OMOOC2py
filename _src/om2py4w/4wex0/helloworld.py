# -*- coding: UTF-8 -*-

from bottle import route, run, template
import sys
#import time
import os
import jamesdiary


data=""


@route('/hello')
def hello():
    return data

def main():
    target = open("diary.txt", 'a+')
    while True:
        line2 = raw_input("history:H, write:Y, quit:N ")
        if line2=="H":
            data=jamesdiary.readdiary()
            run(host='localhost', port=8080,debug=True)
            

        elif line2=="Y":
            data=raw_input("-->")
            jamesdiary.writediary(data)
            run(host='localhost', port=8080,debug=True)
            

        elif line2=="N":
            break

if __name__ == '__main__':
    main()
   



