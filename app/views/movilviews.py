
from flask import render_template,redirect,url_for,request

from main import app
from app.agenservices.dbservice import *
from app.services.mainlightservice import Mainobject,Mainstrip


Bulb1 = Mainobject("192.168.10.25")
Bulb2 = Mainobject("192.168.10.26")

elements = ["O1_cuarto:ip1","O2_cocina:ip2"]
methods = ['off','red','blue','green','white']

'''
for x in elements:
    @app.route(f'/{x}/off')
    def f'{x}.off()':
        print(f"{result}")
        return "Corriste algo"
    
'''
@app.route('/led/off')
def ledoff():
    O5_lampled.off()
    return "<h1> Corriste escena apagar en led </h1>"

@app.route('/led/red')
def ledred():
    O5_lampled.staticred()
    return "<h1> Corriste escena red en led </h1>"

@app.route('/led/blue')
def ledblue():
    O5_lampled.staticblue()
    return "<h1> Corriste escena blue en led </h1>"

@app.route('/led/green')
def ledgreen():
    O5_lampled.staticgreen()
    return "<h1> Corriste escena green en led </h1>"

@app.route('/led/white')
def ledwhite():
    O5_lampled.staticwhite()
    return "<h1> Corriste escena white en led </h1>"

