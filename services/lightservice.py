import asyncio
from kasa import Discover
from kasa import SmartBulb

'''
devices = asyncio.run(Discover.discover())
print("Hello")
print(devices)
for addr, dev in devices.items():
    asyncio.run(dev.update())
    print(f"{addr} >> {dev}")
'''

'''
from pprint import pformat as pf

plug = SmartPlug("192.168.10.158")
asyncio.run(plug.update())
print("Hardware: %s" % pf(plug.hw_info))
print("Full sysinfo: %s" % pf(plug.sys_info))
'''


'''
bulbcocina = SmartBulb("192.168.10.191")
bulbcuarto = SmartBulb("192.168.10.25")
asyncio.run(bulbcocina.update())
'''



'''
status = 1
if status == 0:
    asyncio.run(bulbcocina.turn_off())
    asyncio.run(bulbcuarto.turn_off())
elif status == 1:
    asyncio.run(bulbcocina.turn_on())
    asyncio.run(bulbcuarto.turn_on())
'''
'''
print(bulbcocina.brightness)
asyncio.run(bulbcocina.set_brightness(20))
asyncio.run(bulbcocina.update())
print(bulbcocina.brightness)
'''

#asyncio.run(bulbcocina.set_hsv(180, 100, 100)) #azul
#asyncio.run(bulbcocina.set_hsv(0, 0, 100)) #amarillo
#asyncio.run(bulbcocina.set_hsv(180, 100, 100)) #cyan
#asyncio.run(bulbcocina.set_hsv(120, 100, 100)) #verde
#asyncio.run(bulbcocina.set_hsv(203, 6, 96)) #blanco
#asyncio.run(bulbcocina.set_hsv(0, 100, 100)) #rojo
#asyncio.run(bulbcocina.set_hsv(0, 0, 0)) #amarillo dimeado

'''
import time

for x in range (10):
    asyncio.run(bulbcocina.set_hsv(0, 100, 100)) #azul
    time.sleep(1)
    asyncio.run(bulbcocina.turn_off())
    time.sleep(1)
    print(x)
'''

'''
asyncio.run(bulbcocina.set_hsv(0, 0, 0)) #verde
asyncio.run(bulbcocina.update())
print(bulbcocina)
'''


##query basico a dispositivo
import asyncio
from kasa import SmartPlug
from pprint import pformat as pf

plug = SmartPlug("192.168.10.25")
asyncio.run(plug.update())
print("Hardware: %s" % pf(plug.hw_info))
print("Full sysinfo: %s" % pf(plug.sys_info))

#asyncio.run(plug.update())
#asyncio.run(plug.turn_off())
#asyncio.run(plug.update())
#asyncio.run(plug.set_hsv(180, 100, 100)) #azul notiene este metodo

