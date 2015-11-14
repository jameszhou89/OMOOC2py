# -*- coding: UTF-8 -*-

from bottle import route, run, template
import sys
import time
import os
import jamesdiary


data1=""

def main():
    while True:
        target = open("diary.txt", 'a+')
        line2 = raw_input("history:H, write:Y, quit:N ")
        if line2=="H":
            data1=jamesdiary.readdiary()

            run(host='localhost', port=8080,debug=True)

        elif line2=="Y":
            data1=raw_input("-->")
            jamesdiary.writediary(data1)
    	    run(host='localhost', port=8080,debug=True)

        elif line2=="N":
    	    break



@route('/hello')
def hello():
    return data1

if __name__ == '__main__':
    main()






