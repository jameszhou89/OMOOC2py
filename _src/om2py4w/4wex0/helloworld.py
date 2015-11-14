# -*- coding: UTF-8 -*-

from bottle import route, run, template

@route('/hello')
def hello():
    return "Hello World!中"

if __name__ == "__main__":
    run(host='localhost', port=8080,debug=True)