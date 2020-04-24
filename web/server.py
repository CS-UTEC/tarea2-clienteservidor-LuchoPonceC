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


@app.route('/create_user/<name_>/<full_name_>/<password_>/<username_>')
def create_user(name_,full_name_,password_,username_):
    user = entities.User(
        name = name_,
        fullname = full_name_,
        password = password_,
        username = username_,
    )
    print(user)
    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()
    return "user createrd!"


@app.route('/read_user')
def read_userds():
    db_session = db.getSession(engine)
    respuesta = db_session.query(entities.User)
    users = respuesta[:]
    #print(len(users))
    devolver = "<table><tr>"
    lista_atributos = ["Name","Full name","Password","Username"]
    
    for i in lista_atributos:
        devolver+="<th>"+str(i)+"</th>"
    devolver+="</tr>"
    for i in range(len(users)):
        devolver += "<tr><td>"+users[i].name+"</td>"
        devolver += "<td>"+users[i].fullname+"</td>"
        devolver += "<td>"+users[i].password+"</td>"
        devolver += "<td>"+users[i].username+"</td></tr>"
    devolver+="</table>"
    return devolver




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=80, threaded=True, host=('127.0.0.1'))
