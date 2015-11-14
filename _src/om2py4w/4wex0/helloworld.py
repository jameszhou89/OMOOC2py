# -*- coding: UTF-8 -*-

from bottle import route, run, template

data=""

@route('/hello')
def hello(data):
    return data


def main();
    while True:
        line2 = raw_input("if you want to continue print Y, want to quit print N ")
        if line2=="Y":
            data=raw_input("-->")
    	    run(host='localhost', port=8080,debug=True)
        elif line2=="N":
    	    break


if __name__ == "__main__":
    main（）