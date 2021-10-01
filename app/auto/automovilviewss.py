#//[This is an Autofile by GMAN]
from main import app
from app.agenservices.dbservice import *
from app.services.mainlightservice import Mainobject,Mainstrip
A1 = Mainobject('192.168.20.11')
A2 = Mainobject('192.168.20.12')

#--------------------BULB---------------------A1
@app.route("/A1/red")
def A1red():
   A1.red()
   return "<h1> Corriste escena red en A1 </h1>"
@app.route("/A1/blue")
def A1blue():
   A1.blue()
   return "<h1> Corriste escena blue en A1 </h1>"
@app.route("/A1/off")
def A1off():
   A1.off()
   return "<h1> Corriste escena off en A1 </h1>"
@app.route("/A1/white")
def A1white():
   A1.white()
   return "<h1> Corriste escena white en A1 </h1>"
@app.route("/A1/green")
def A1green():
   A1.green()
   return "<h1> Corriste escena green en A1 </h1>"
#--------------------BULB---------------------A2
@app.route("/A2/red")
def A2red():
   A2.red()
   return "<h1> Corriste escena red en A2 </h1>"
@app.route("/A2/blue")
def A2blue():
   A2.blue()
   return "<h1> Corriste escena blue en A2 </h1>"
@app.route("/A2/off")
def A2off():
   A2.off()
   return "<h1> Corriste escena off en A2 </h1>"
@app.route("/A2/white")
def A2white():
   A2.white()
   return "<h1> Corriste escena white en A2 </h1>"
@app.route("/A2/green")
def A2green():
   A2.green()
   return "<h1> Corriste escena green en A2 </h1>"


