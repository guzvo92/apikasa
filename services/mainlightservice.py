import asyncio
import time
from kasa import Discover
from kasa import SmartBulb
from kasa import SmartLightStrip

class Mainobject:
    
    def __init__(self,ip):
        try:
            self.target = SmartBulb(ip)
            print("Conexion creada ip:"+str(ip))    
        except:
            print("no se creo la conexion"+str(ip))

    def off(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.turn_off())

    def staticred(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(0, 100, 100)) #rojo

    def staticblue(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(180, 100, 100)) #cyan

    def staticgreen(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(120, 100, 100)) #green

    def staticwhite(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(203, 6, 96)) #blanco


    def alarmablue(self):
        asyncio.run(self.target.update())
        for x in range (10):
            asyncio.run(self.target.set_hsv(0, 100, 100)) #azul
            time.sleep(1)
            asyncio.run(self.target.turn_off())
            time.sleep(1)
            print(x)


class Mainstrip:
    
    def __init__(self,ip):
        try:
            self.target = SmartLightStrip(ip)
            print("Conexion creada ip:"+str(ip))    
        except:
            print("no se creo la conexion"+str(ip))
   
    def off(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.turn_off())

    def staticred(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(0, 100, 100)) #rojo

    def staticblue(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(180, 100, 100)) #cyan

    def staticgreen(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(120, 100, 100)) #green

    def staticwhite(self):
        asyncio.run(self.target.update())
        asyncio.run(self.target.set_hsv(203, 6, 96)) #blanco


    def alarmablue(self):
        asyncio.run(self.target.update())
        for x in range (10):
            asyncio.run(self.target.set_hsv(0, 100, 100)) #azul
            time.sleep(1)
            asyncio.run(self.target.turn_off())
            time.sleep(1)
            print(x)
