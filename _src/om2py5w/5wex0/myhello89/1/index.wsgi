 # coding:utf-8
from bottle import Bottle, run
import sys
import sae


app = Bottle()

@app.route('/')
def hello():
    return "Hello, world! - good night Bottle"



application = sae.create_wsgi_app(app)