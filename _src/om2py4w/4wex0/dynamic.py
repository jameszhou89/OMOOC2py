# -*- coding: UTF-8 -*-
from bottle import route, run, template

data=""

@route('/hello')
def hello():
    return data

if __name__ == "__main__":
    while True:
        line2 = raw_input("continue print Y, want to quit print N ")
        if line2=="Y":
            data=raw_input("-->")
            run(host='localhost', port=8080,debug=True)
        elif line2=="N":
            break