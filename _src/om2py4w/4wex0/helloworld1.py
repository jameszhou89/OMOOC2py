# -*- coding: UTF-8 -*-
from bottle import route, run, template,debug,get,post,request
import sys
import time
import os
import jamesdiary


@route('/write')
def write():
    return '''
        <form action="/write" method="post">
            writediary: <input name="writediary1" type="text" />
            <input value="save" type="submit" />
        </form>
    '''


@route('/write', method='POST')
def do_write():
    writediary1= request.forms.get('writediary1')
    jamesdiary.writediary(writediary1)
    if writediary1:
        return template("<p>You are now writing {{diary}} into your diary.</p>", diary=writediary1)

@route("/read")
def read():
    target = open("diary.txt")
    content=jamesdiary.readdiary()
    return content

debug(True)
run(host='localhost', port=8080,debug=True)

   



