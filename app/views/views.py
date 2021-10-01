#views kazapypy

from flask import render_template,redirect,url_for,request

from main import app
from app.agenservices.dbservice import *

from app.agenservices.makerservice import Crearutas

def rutinadepa():
    
    O1 = {'name':'cuarto','type':'bulb','ip':'192.168.10.25'}
    O2 = {'name':'cocina','type':'bulb','ip':'192.168.10.26'}
    O3 = {'name':'led','type':'strip','ip':'192.168.10.115'}

    items = [O1,O2,O3]
    arraymethods = {'off','red','blue','green','white'}
    Crearutas(items,arraymethods,'app/auto/autodepaviews.py')

def rutinamovil():
    
    O1 = {'name':'A1','type':'bulb','ip':'192.168.20.11'}
    O2 = {'name':'A2','type':'bulb','ip':'192.168.20.12'}

    items = [O1,O2]
    arraymethods = {'off','red','blue','green','white'}
    Crearutas(items,arraymethods,'app/auto/automovilviewss.py')


depa_status = 1

if depa_status == 0:
    rutinadepa()
    from app.auto.autodepaviews import *
elif depa_status == 1: 
    rutinamovil()
    from app.auto.automovilviewss import *

#//rutas tienen que estar vinculadas a un metodo
@app.route('/home')
def home(): 
    return "<h1> Esta es la pagina home </h1>"

@app.route('/admin')
def admin():
    dates="date"
    itemshome = [O1_cuarto,O2_cocina,O3_lampder,O4_lampizq]

    return render_template('index.html',
                                items=itemshome,date=dates,
                                )



