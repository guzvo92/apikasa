#//[This is an Autofile by GMAN]
from main import app
from app.agenservices.dbservice import *
from app.services.mainlightservice import Mainobject,Mainstrip
A1 = Mainobject('192.168.15.11')
A2 = Mainobject('192.168.15.12')
A3 = Mainobject('192.168.15.13')
A4 = Mainobject('192.168.15.14')
A5 = Mainobject('192.168.15.15')
A6 = Mainobject('192.168.15.16')
A7 = Mainobject('192.168.15.17')
A8 = Mainobject('192.168.15.18')

#--------------------BULB---------------------A1
@app.route("/A1/green")
def A1green():
   A1.green()
   return "<h1> Corriste escena green en A1 </h1>"
@app.route("/A1/red")
def A1red():
   A1.red()
   return "<h1> Corriste escena red en A1 </h1>"
@app.route("/A1/white")
def A1white():
   A1.white()
   return "<h1> Corriste escena white en A1 </h1>"
@app.route("/A1/blue")
def A1blue():
   A1.blue()
   return "<h1> Corriste escena blue en A1 </h1>"
@app.route("/A1/off")
def A1off():
   A1.off()
   return "<h1> Corriste escena off en A1 </h1>"
#--------------------BULB---------------------A2
@app.route("/A2/green")
def A2green():
   A2.green()
   return "<h1> Corriste escena green en A2 </h1>"
@app.route("/A2/red")
def A2red():
   A2.red()
   return "<h1> Corriste escena red en A2 </h1>"
@app.route("/A2/white")
def A2white():
   A2.white()
   return "<h1> Corriste escena white en A2 </h1>"
@app.route("/A2/blue")
def A2blue():
   A2.blue()
   return "<h1> Corriste escena blue en A2 </h1>"
@app.route("/A2/off")
def A2off():
   A2.off()
   return "<h1> Corriste escena off en A2 </h1>"
#--------------------BULB---------------------A3
@app.route("/A3/green")
def A3green():
   A3.green()
   return "<h1> Corriste escena green en A3 </h1>"
@app.route("/A3/red")
def A3red():
   A3.red()
   return "<h1> Corriste escena red en A3 </h1>"
@app.route("/A3/white")
def A3white():
   A3.white()
   return "<h1> Corriste escena white en A3 </h1>"
@app.route("/A3/blue")
def A3blue():
   A3.blue()
   return "<h1> Corriste escena blue en A3 </h1>"
@app.route("/A3/off")
def A3off():
   A3.off()
   return "<h1> Corriste escena off en A3 </h1>"
#--------------------BULB---------------------A4
@app.route("/A4/green")
def A4green():
   A4.green()
   return "<h1> Corriste escena green en A4 </h1>"
@app.route("/A4/red")
def A4red():
   A4.red()
   return "<h1> Corriste escena red en A4 </h1>"
@app.route("/A4/white")
def A4white():
   A4.white()
   return "<h1> Corriste escena white en A4 </h1>"
@app.route("/A4/blue")
def A4blue():
   A4.blue()
   return "<h1> Corriste escena blue en A4 </h1>"
@app.route("/A4/off")
def A4off():
   A4.off()
   return "<h1> Corriste escena off en A4 </h1>"
#--------------------BULB---------------------A5
@app.route("/A5/green")
def A5green():
   A5.green()
   return "<h1> Corriste escena green en A5 </h1>"
@app.route("/A5/red")
def A5red():
   A5.red()
   return "<h1> Corriste escena red en A5 </h1>"
@app.route("/A5/white")
def A5white():
   A5.white()
   return "<h1> Corriste escena white en A5 </h1>"
@app.route("/A5/blue")
def A5blue():
   A5.blue()
   return "<h1> Corriste escena blue en A5 </h1>"
@app.route("/A5/off")
def A5off():
   A5.off()
   return "<h1> Corriste escena off en A5 </h1>"
#--------------------BULB---------------------A6
@app.route("/A6/green")
def A6green():
   A6.green()
   return "<h1> Corriste escena green en A6 </h1>"
@app.route("/A6/red")
def A6red():
   A6.red()
   return "<h1> Corriste escena red en A6 </h1>"
@app.route("/A6/white")
def A6white():
   A6.white()
   return "<h1> Corriste escena white en A6 </h1>"
@app.route("/A6/blue")
def A6blue():
   A6.blue()
   return "<h1> Corriste escena blue en A6 </h1>"
@app.route("/A6/off")
def A6off():
   A6.off()
   return "<h1> Corriste escena off en A6 </h1>"
#--------------------BULB---------------------A7
@app.route("/A7/green")
def A7green():
   A7.green()
   return "<h1> Corriste escena green en A7 </h1>"
@app.route("/A7/red")
def A7red():
   A7.red()
   return "<h1> Corriste escena red en A7 </h1>"
@app.route("/A7/white")
def A7white():
   A7.white()
   return "<h1> Corriste escena white en A7 </h1>"
@app.route("/A7/blue")
def A7blue():
   A7.blue()
   return "<h1> Corriste escena blue en A7 </h1>"
@app.route("/A7/off")
def A7off():
   A7.off()
   return "<h1> Corriste escena off en A7 </h1>"
#--------------------BULB---------------------A8
@app.route("/A8/green")
def A8green():
   A8.green()
   return "<h1> Corriste escena green en A8 </h1>"
@app.route("/A8/red")
def A8red():
   A8.red()
   return "<h1> Corriste escena red en A8 </h1>"
@app.route("/A8/white")
def A8white():
   A8.white()
   return "<h1> Corriste escena white en A8 </h1>"
@app.route("/A8/blue")
def A8blue():
   A8.blue()
   return "<h1> Corriste escena blue en A8 </h1>"
@app.route("/A8/off")
def A8off():
   A8.off()
   return "<h1> Corriste escena off en A8 </h1>"


