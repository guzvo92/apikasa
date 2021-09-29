#//[This is an Autofile by GMAN]
from main import app
from app.agenservices.dbservice import *
from app.services.mainlightservice import Mainobject,Mainstrip
cuarto = Mainobject('192.168.10.25')
cocina = Mainobject('192.168.10.26')
led = Mainstrip('192.168.10.115')

#--------------------BULB---------------------cuarto
@app.route("/cuarto/green")
def cuartogreen():
   cuarto.green()
   return "<h1> Corriste escena green en cuarto </h1>"
@app.route("/cuarto/blue")
def cuartoblue():
   cuarto.blue()
   return "<h1> Corriste escena blue en cuarto </h1>"
@app.route("/cuarto/red")
def cuartored():
   cuarto.red()
   return "<h1> Corriste escena red en cuarto </h1>"
@app.route("/cuarto/off")
def cuartooff():
   cuarto.off()
   return "<h1> Corriste escena off en cuarto </h1>"
@app.route("/cuarto/white")
def cuartowhite():
   cuarto.white()
   return "<h1> Corriste escena white en cuarto </h1>"
#--------------------BULB---------------------cocina
@app.route("/cocina/green")
def cocinagreen():
   cocina.green()
   return "<h1> Corriste escena green en cocina </h1>"
@app.route("/cocina/blue")
def cocinablue():
   cocina.blue()
   return "<h1> Corriste escena blue en cocina </h1>"
@app.route("/cocina/red")
def cocinared():
   cocina.red()
   return "<h1> Corriste escena red en cocina </h1>"
@app.route("/cocina/off")
def cocinaoff():
   cocina.off()
   return "<h1> Corriste escena off en cocina </h1>"
@app.route("/cocina/white")
def cocinawhite():
   cocina.white()
   return "<h1> Corriste escena white en cocina </h1>"
#--------------------STRIP---------------------led
@app.route("/led/green")
def ledgreen():
   led.green()
   return "<h1> Corriste escena green en led </h1>"
@app.route("/led/blue")
def ledblue():
   led.blue()
   return "<h1> Corriste escena blue en led </h1>"
@app.route("/led/red")
def ledred():
   led.red()
   return "<h1> Corriste escena red en led </h1>"
@app.route("/led/off")
def ledoff():
   led.off()
   return "<h1> Corriste escena off en led </h1>"
@app.route("/led/white")
def ledwhite():
   led.white()
   return "<h1> Corriste escena white en led </h1>"


