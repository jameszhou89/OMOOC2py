 # coding:utf-8
from bottle import Bottle, run

import sae
import sys

app = Bottle()

@app.route('/')
def hello():
    return "Hello, world! - Bottle"

application = sae.create_wsgi_app(app)