#views kazapypy

from flask import render_template,redirect,url_for,request

from main import app
from agenservices.dbservice import *
from services.mainlightservice import Mainobject,Mainstrip


#x = Maindb('test.db')
#x.desco()

O1_cuarto = Mainobject("192.168.20.11")
O2_cocina = Mainobject("192.168.20.12")

##O1_cuarto = Mainobject("192.168.10.25")
#O2_cocina = Mainobject("192.168.10.26")
O3_lampder = Mainobject("192.168.10.27")
O4_lampizq = Mainobject("192.168.10.28")
O5_lampled = Mainstrip("192.168.10.115")

def staticred(target):
    asyncio.run(target.update())
    asyncio.run(target.set_hsv(0, 100, 100)) #rojo

def staticblue(target):
    asyncio.run(target.update())
    asyncio.run(target.set_hsv(180, 100, 100)) #cyan

#//rutas tienen que estar vinculadas a un metodo
@app.route('/home')
def home(): 
    return "<h1> Esta es la pagina home </h1>"

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

#--------------------------------------------------

@app.route('/cuarto/off')
def cuartooff():
    O1_cuarto.off()
    return "<h1> Corriste escena apagar en cuarto </h1>"

@app.route('/cuarto/red')
def cuartored():
    O1_cuarto.staticred()
    return "<h1> Corriste escena red en cuarto </h1>"

@app.route('/cuarto/blue')
def cuartoblue():
    O1_cuarto.staticblue()
    return "<h1> Corriste escena blue en cuarto </h1>"

@app.route('/cuarto/green')
def cuartogreen():
    O1_cuarto.staticgreen()
    return "<h1> Corriste escena green en cuarto </h1>"

@app.route('/cuarto/white')
def cuartowhite():
    O1_cuarto.staticwhite()
    return "<h1> Corriste escena white en cuarto </h1>"



@app.route('/cocina/off')
def cocinaoff():
    O2_cocina.off()
    return "<h1> Corriste escena apagar en cocina </h1>"

@app.route('/cocina/red')
def cocinared():
    O2_cocina.staticred()
    return "<h1> Corriste escena red en cocina </h1>"

@app.route('/cocina/blue')
def cocinablue():
    O2_cocina.staticblue()
    return "<h1> Corriste escena blue en cocina </h1>"

@app.route('/cocina/green')
def cocinagreen():
    O2_cocina.staticgreen()
    return "<h1> Corriste escena green en cocina </h1>"

@app.route('/cocina/white')
def cocinawhite():
    O2_cocina.staticwhite()
    return "<h1> Corriste escena white en cocina </h1>"

@app.route('/cocina/alarma')
def alarmablue():
    O2_cocina.alarmablue()
    return "<h1> Corriste escena alarmablue en cocina </h1>"




@app.route('/admin')
def admin():
    dates="date"
    itemshome = [O1_cuarto,O2_cocina,O3_lampder,O4_lampizq]

    return render_template('index.html',
                                items=itemshome,date=dates,
                                )


