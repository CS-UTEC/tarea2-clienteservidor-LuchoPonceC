from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time
import math
db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/palindromo/<content>')
def palindromo(content): 
    return str(str(content) == ''.join(reversed((content))))


@app.route('/multiplo/<content1>/<content2>')
def multiplo(content1,content2): 
    maximo=max(int(content1),int(content2))
    minimo=min(int(content1),int(content2))
    return "NO lo son" if maximo%minimo!=0 else "Si lo son"
     


    return str(str(content) == ''.join(reversed((content))))





if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
