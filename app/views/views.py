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
    
    O1 = {'name':'A1','type':'bulb','ip':'192.168.15.11'}
    O2 = {'name':'A2','type':'bulb','ip':'192.168.15.12'}
    O3 = {'name':'A3','type':'bulb','ip':'192.168.15.13'}
    O4 = {'name':'A4','type':'bulb','ip':'192.168.15.14'}
    O5 = {'name':'A5','type':'bulb','ip':'192.168.15.15'}
    O6 = {'name':'A6','type':'bulb','ip':'192.168.15.16'}
    O7 = {'name':'A7','type':'bulb','ip':'192.168.15.17'}
    O8 = {'name':'A8','type':'bulb','ip':'192.168.15.18'}


    items = [O1,O2,O3,O4,O5,O6,O7,O8]
    arraymethods = {'off','red','blue','green','white'}
    Crearutas(items,arraymethods,'/srv/apikasa/app/auto/automovilviews.py')
    #Crearutas(items,arraymethods,'app/auto/automovilviews.py')

    #---------------------------------------------------------------------------
    from app.services.mainlightservice import Mainobject,Mainstrip
    import time

    A1 = Mainobject('192.168.15.11')
    A2 = Mainobject('192.168.15.12')
    A3 = Mainobject('192.168.15.13')
    A4 = Mainobject('192.168.15.14')
    A5 = Mainobject('192.168.15.15')
    A6 = Mainobject('192.168.15.16')
    A7 = Mainobject('192.168.15.17')
    A8 = Mainobject('192.168.15.18')

    sleeptime = 0.3
    @app.route("/all/off")
    def alloff():
        A1.off()
        time.sleep(sleeptime)
        A2.off()
        time.sleep(sleeptime)
        A3.off()
        time.sleep(sleeptime)
        A4.off()
        time.sleep(sleeptime)
        A5.off()
        time.sleep(sleeptime)
        A6.off()
        time.sleep(sleeptime)
        A7.off()
        time.sleep(sleeptime)
        A8.off()
        return "<h1> Corriste escena all off </h1>"

    @app.route("/all/blue")
    def allblue():
        A1.blue()
        time.sleep(sleeptime)
        A2.blue()
        time.sleep(sleeptime)
        A3.blue()
        time.sleep(sleeptime)
        A4.blue()
        time.sleep(sleeptime)
        A5.blue()
        time.sleep(sleeptime)
        A6.blue()
        time.sleep(sleeptime)
        A7.blue()
        time.sleep(sleeptime)
        A8.blue()
        return "<h1> Corriste escena all blue </h1>"

    @app.route("/all/red")
    def allred():
        A1.red()
        time.sleep(sleeptime)
        A2.red()
        time.sleep(sleeptime)
        A3.red()
        time.sleep(sleeptime)
        A4.red()
        time.sleep(sleeptime)
        A5.red()
        time.sleep(sleeptime)
        A6.red()
        time.sleep(sleeptime)
        A7.red()
        time.sleep(sleeptime)
        A8.red()
        return "<h1> Corriste escena all red </h1>"

depa_status = 1

if depa_status == 0:
    rutinadepa()
    from app.auto.autodepaviews import *
elif depa_status == 1: 
    rutinamovil()
    from app.auto.automovilviews import *

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



