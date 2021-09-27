import asyncio
from kasa import Discover
from kasa import SmartBulb
from kasa import SmartPlug
from kasa import SmartStrip
from kasa import SmartLightStrip

from pprint import pformat as pf

plug = SmartLightStrip("192.168.10.115")
asyncio.run(plug.update())
#asyncio.run(plug.turn_off())
#asyncio.run(plug.turn_on())
#asyncio.run(plug.set_hsv(0, 100, 100))

#dict is not callable
#asyncio.run(plug.effect({'brightness': 30,'custom': 0,'enable': 0,'id': 'oJjUMosgEMrdumfPANKbkFmBcAdEQsPy','name': 'ocean'}))