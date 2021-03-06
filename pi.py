import RPi.GPIO as GPIO #Librería para controlar GPIO
import time #Librería para funciones relacionadas con tiempo (sleep)
import requests
'''
rs1b = requests.get('https://192.168.10.101:2600/s1/blue')
rs1r = requests.get('https://192.168.10.101:2600/s1/red')
rs1w = requests.get('https://192.168.10.101:2600/s1/white')
rs1o = requests.get('https://192.168.10.101:2600/s1/off')
'''

GPIO.setmode(GPIO.BCM) #Simplemente nos sirve para usar números de pin de placa y no del procesador
GPIO.setwarnings(False) #Con esto impedimos que nos aparezcan warnings que en este caso no serán importantes

b1 = 25 #Variable donde ponemos el pin que usaremos para el LED
b2 = 12 ##Variable donde ponemos el pin que usaremos para el pulsador
b3 = 21 ##Variable donde ponemos el pin que usaremos para el pulsador


#GPIO.setup(b1, GPIO.OUT) #Configuramos el pin 21 (led) como salida
GPIO.setup(b1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(b2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(b3, GPIO.IN, GPIO.PUD_UP) #Configuramos el pin 13 (btn) como entrada con resistencia de pull up

while True:
    tiempo = 0.2

    if GPIO.input(b1) == False:
        print ("Pulsador1 está pulsado")
        requests.get('http://192.168.15.11:2600/all/blue')
    else:
        pass
    
    if GPIO.input(b2) == False:
        print ("Pulsador2 está pulsado")
        requests.get('http://192.168.15.11:2600/all/red')
    else:
        pass

    if GPIO.input(b3) == False:
        print ("Pulsador3 está pulsado")
        requests.get('http://192.168.15.11:2600/all/white')
    else:
        pass

    time.sleep(tiempo) #Esperamos un tiempo para que se vea el parpadeo del LED
    
    #GPIO.output(led,1) #Encendemos el LED

    #time.sleep(tiempo) #Esperamos un tiempo para que se vea el parpadeo del LED

    #GPIO.output(led,0) #Apagamos el LED

GPIO.cleanup()