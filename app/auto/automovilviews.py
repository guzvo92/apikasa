#//[This is an Autofile by GMAN]
from main import app
from app.agenservices.dbservice import *
from app.services.mainlightservice import Mainobject,Mainstrip
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

#--------------------BULB---------------------a1
@app.route("/a1/alarmwhite")
def a1alarmwhite():
   a1.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a1 </h1>"
@app.route("/a1/green")
def a1green():
   a1.green()
   return "<h1> Corriste escena green en a1 </h1>"
@app.route("/a1/blue")
def a1blue():
   a1.blue()
   return "<h1> Corriste escena blue en a1 </h1>"
@app.route("/a1/off")
def a1off():
   a1.off()
   return "<h1> Corriste escena off en a1 </h1>"
@app.route("/a1/red")
def a1red():
   a1.red()
   return "<h1> Corriste escena red en a1 </h1>"
@app.route("/a1/alarmblue")
def a1alarmblue():
   a1.alarmblue()
   return "<h1> Corriste escena alarmblue en a1 </h1>"
@app.route("/a1/white")
def a1white():
   a1.white()
   return "<h1> Corriste escena white en a1 </h1>"
#--------------------BULB---------------------a2
@app.route("/a2/alarmwhite")
def a2alarmwhite():
   a2.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a2 </h1>"
@app.route("/a2/green")
def a2green():
   a2.green()
   return "<h1> Corriste escena green en a2 </h1>"
@app.route("/a2/blue")
def a2blue():
   a2.blue()
   return "<h1> Corriste escena blue en a2 </h1>"
@app.route("/a2/off")
def a2off():
   a2.off()
   return "<h1> Corriste escena off en a2 </h1>"
@app.route("/a2/red")
def a2red():
   a2.red()
   return "<h1> Corriste escena red en a2 </h1>"
@app.route("/a2/alarmblue")
def a2alarmblue():
   a2.alarmblue()
   return "<h1> Corriste escena alarmblue en a2 </h1>"
@app.route("/a2/white")
def a2white():
   a2.white()
   return "<h1> Corriste escena white en a2 </h1>"
#--------------------BULB---------------------a3
@app.route("/a3/alarmwhite")
def a3alarmwhite():
   a3.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a3 </h1>"
@app.route("/a3/green")
def a3green():
   a3.green()
   return "<h1> Corriste escena green en a3 </h1>"
@app.route("/a3/blue")
def a3blue():
   a3.blue()
   return "<h1> Corriste escena blue en a3 </h1>"
@app.route("/a3/off")
def a3off():
   a3.off()
   return "<h1> Corriste escena off en a3 </h1>"
@app.route("/a3/red")
def a3red():
   a3.red()
   return "<h1> Corriste escena red en a3 </h1>"
@app.route("/a3/alarmblue")
def a3alarmblue():
   a3.alarmblue()
   return "<h1> Corriste escena alarmblue en a3 </h1>"
@app.route("/a3/white")
def a3white():
   a3.white()
   return "<h1> Corriste escena white en a3 </h1>"
#--------------------BULB---------------------a4
@app.route("/a4/alarmwhite")
def a4alarmwhite():
   a4.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a4 </h1>"
@app.route("/a4/green")
def a4green():
   a4.green()
   return "<h1> Corriste escena green en a4 </h1>"
@app.route("/a4/blue")
def a4blue():
   a4.blue()
   return "<h1> Corriste escena blue en a4 </h1>"
@app.route("/a4/off")
def a4off():
   a4.off()
   return "<h1> Corriste escena off en a4 </h1>"
@app.route("/a4/red")
def a4red():
   a4.red()
   return "<h1> Corriste escena red en a4 </h1>"
@app.route("/a4/alarmblue")
def a4alarmblue():
   a4.alarmblue()
   return "<h1> Corriste escena alarmblue en a4 </h1>"
@app.route("/a4/white")
def a4white():
   a4.white()
   return "<h1> Corriste escena white en a4 </h1>"
#--------------------BULB---------------------a5
@app.route("/a5/alarmwhite")
def a5alarmwhite():
   a5.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a5 </h1>"
@app.route("/a5/green")
def a5green():
   a5.green()
   return "<h1> Corriste escena green en a5 </h1>"
@app.route("/a5/blue")
def a5blue():
   a5.blue()
   return "<h1> Corriste escena blue en a5 </h1>"
@app.route("/a5/off")
def a5off():
   a5.off()
   return "<h1> Corriste escena off en a5 </h1>"
@app.route("/a5/red")
def a5red():
   a5.red()
   return "<h1> Corriste escena red en a5 </h1>"
@app.route("/a5/alarmblue")
def a5alarmblue():
   a5.alarmblue()
   return "<h1> Corriste escena alarmblue en a5 </h1>"
@app.route("/a5/white")
def a5white():
   a5.white()
   return "<h1> Corriste escena white en a5 </h1>"
#--------------------BULB---------------------a6
@app.route("/a6/alarmwhite")
def a6alarmwhite():
   a6.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a6 </h1>"
@app.route("/a6/green")
def a6green():
   a6.green()
   return "<h1> Corriste escena green en a6 </h1>"
@app.route("/a6/blue")
def a6blue():
   a6.blue()
   return "<h1> Corriste escena blue en a6 </h1>"
@app.route("/a6/off")
def a6off():
   a6.off()
   return "<h1> Corriste escena off en a6 </h1>"
@app.route("/a6/red")
def a6red():
   a6.red()
   return "<h1> Corriste escena red en a6 </h1>"
@app.route("/a6/alarmblue")
def a6alarmblue():
   a6.alarmblue()
   return "<h1> Corriste escena alarmblue en a6 </h1>"
@app.route("/a6/white")
def a6white():
   a6.white()
   return "<h1> Corriste escena white en a6 </h1>"
#--------------------BULB---------------------a7
@app.route("/a7/alarmwhite")
def a7alarmwhite():
   a7.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a7 </h1>"
@app.route("/a7/green")
def a7green():
   a7.green()
   return "<h1> Corriste escena green en a7 </h1>"
@app.route("/a7/blue")
def a7blue():
   a7.blue()
   return "<h1> Corriste escena blue en a7 </h1>"
@app.route("/a7/off")
def a7off():
   a7.off()
   return "<h1> Corriste escena off en a7 </h1>"
@app.route("/a7/red")
def a7red():
   a7.red()
   return "<h1> Corriste escena red en a7 </h1>"
@app.route("/a7/alarmblue")
def a7alarmblue():
   a7.alarmblue()
   return "<h1> Corriste escena alarmblue en a7 </h1>"
@app.route("/a7/white")
def a7white():
   a7.white()
   return "<h1> Corriste escena white en a7 </h1>"
#--------------------BULB---------------------a8
@app.route("/a8/alarmwhite")
def a8alarmwhite():
   a8.alarmwhite()
   return "<h1> Corriste escena alarmwhite en a8 </h1>"
@app.route("/a8/green")
def a8green():
   a8.green()
   return "<h1> Corriste escena green en a8 </h1>"
@app.route("/a8/blue")
def a8blue():
   a8.blue()
   return "<h1> Corriste escena blue en a8 </h1>"
@app.route("/a8/off")
def a8off():
   a8.off()
   return "<h1> Corriste escena off en a8 </h1>"
@app.route("/a8/red")
def a8red():
   a8.red()
   return "<h1> Corriste escena red en a8 </h1>"
@app.route("/a8/alarmblue")
def a8alarmblue():
   a8.alarmblue()
   return "<h1> Corriste escena alarmblue en a8 </h1>"
@app.route("/a8/white")
def a8white():
   a8.white()
   return "<h1> Corriste escena white en a8 </h1>"
#--------------------STRIP---------------------s1
@app.route("/s1/alarmwhite")
def s1alarmwhite():
   s1.alarmwhite()
   return "<h1> Corriste escena alarmwhite en s1 </h1>"
@app.route("/s1/green")
def s1green():
   s1.green()
   return "<h1> Corriste escena green en s1 </h1>"
@app.route("/s1/blue")
def s1blue():
   s1.blue()
   return "<h1> Corriste escena blue en s1 </h1>"
@app.route("/s1/off")
def s1off():
   s1.off()
   return "<h1> Corriste escena off en s1 </h1>"
@app.route("/s1/red")
def s1red():
   s1.red()
   return "<h1> Corriste escena red en s1 </h1>"
@app.route("/s1/alarmblue")
def s1alarmblue():
   s1.alarmblue()
   return "<h1> Corriste escena alarmblue en s1 </h1>"
@app.route("/s1/white")
def s1white():
   s1.white()
   return "<h1> Corriste escena white en s1 </h1>"
#--------------------STRIP---------------------s2
@app.route("/s2/alarmwhite")
def s2alarmwhite():
   s2.alarmwhite()
   return "<h1> Corriste escena alarmwhite en s2 </h1>"
@app.route("/s2/green")
def s2green():
   s2.green()
   return "<h1> Corriste escena green en s2 </h1>"
@app.route("/s2/blue")
def s2blue():
   s2.blue()
   return "<h1> Corriste escena blue en s2 </h1>"
@app.route("/s2/off")
def s2off():
   s2.off()
   return "<h1> Corriste escena off en s2 </h1>"
@app.route("/s2/red")
def s2red():
   s2.red()
   return "<h1> Corriste escena red en s2 </h1>"
@app.route("/s2/alarmblue")
def s2alarmblue():
   s2.alarmblue()
   return "<h1> Corriste escena alarmblue en s2 </h1>"
@app.route("/s2/white")
def s2white():
   s2.white()
   return "<h1> Corriste escena white en s2 </h1>"


