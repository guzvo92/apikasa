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
    
    O1 = {'name':'a1','type':'bulb','ip':'192.168.15.11'}
    O2 = {'name':'a2','type':'bulb','ip':'192.168.15.12'}
    O3 = {'name':'a3','type':'bulb','ip':'192.168.15.13'}
    O4 = {'name':'a4','type':'bulb','ip':'192.168.15.14'}
    O5 = {'name':'a5','type':'bulb','ip':'192.168.15.15'}
    O6 = {'name':'a6','type':'bulb','ip':'192.168.15.16'}
    O7 = {'name':'a7','type':'bulb','ip':'192.168.15.17'}
    O8 = {'name':'a8','type':'bulb','ip':'192.168.15.18'}

    S1 = {'name':'s1','type':'strip','ip':'192.168.15.31'}
    S2 = {'name':'s2','type':'strip','ip':'192.168.15.32'}


    items = [O1,O2,O3,O4,O5,O6,O7,O8,S1,S2]
    arraymethods = {'off','red','blue','green','white','alarmblue','alarmwhite'}
    #Crearutas(items,arraymethods,'/srv/apikasa/app/auto/automovilviews.py')
    Crearutas(items,arraymethods,'app/auto/automovilviews.py')

    #---------------------------------------------------------------------------
    from app.services.mainlightservice import Mainobject,Mainstrip
    import time

    a1 = Mainobject('192.168.15.11')
    a2 = Mainobject('192.168.15.12')
    a3 = Mainobject('192.168.15.13')
    a4 = Mainobject('192.168.15.14')
    a5 = Mainobject('192.168.15.15')
    a6 = Mainobject('192.168.15.16')
    a7 = Mainobject('192.168.15.17')
    a8 = Mainobject('192.168.15.18')
    s1 = Mainstrip('192.168.15.31')
    s2 = Mainstrip('192.168.15.32')

    sleeptime = 0.3

    def genallblue():
        a1.blue()
        time.sleep(sleeptime)
        a2.blue()
        time.sleep(sleeptime)
        a3.blue()
        time.sleep(sleeptime)
        a4.blue()
        time.sleep(sleeptime)
        a5.blue()
        time.sleep(sleeptime)
        a6.blue()    
        time.sleep(sleeptime)
        a7.blue()
        time.sleep(sleeptime)
        a8.blue()
        s1.alarmblue()

    def genalloff():
        a1.off()
        time.sleep(sleeptime)
        a2.off()
        time.sleep(sleeptime)
        a3.off()
        time.sleep(sleeptime)
        a4.off()
        time.sleep(sleeptime)
        a5.off()
        time.sleep(sleeptime)
        a6.off()
        time.sleep(sleeptime)
        a7.off()
        time.sleep(sleeptime)
        a8.off()

    def genallred():
        a1.red()
        time.sleep(sleeptime)
        a2.red()
        time.sleep(sleeptime)
        a3.red()
        time.sleep(sleeptime)
        a4.red()
        time.sleep(sleeptime)
        a5.red()
        time.sleep(sleeptime)
        a6.red()
        time.sleep(sleeptime)
        a7.red()
        time.sleep(sleeptime)
        a8.red()
        s1.alarmred()
    

    @app.route("/all/off")
    def alloff():
        genalloff()
        s1.off()
        return "<h1> Corriste escena all off </h1>"

    @app.route("/all/blue")
    def allblue():
        genallblue()
        genalloff()
        s1.off()
        return "<h1> Corriste escena all blue </h1>"

    @app.route("/all/red")
    def allred():
        genallred()
        genalloff()
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



