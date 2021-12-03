import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  #Para usar números de pin de placa y no del procesador
GPIO.setwarnings(False) #Impedir popups de warnings no importantes en este caso


led = 21
boton = 16
GPIO.setup(led, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(boton, GPIO.IN, GPIO.PUD_UP)
import time
while True:

    if GPIO.input(led) == False:
        time.sleep(2)
        print("falso led oprimido")
    else:
        time.sleep(2)
        print("nada en el led")

    if GPIO.input(boton) == False:
        time.sleep(2)
        print("falso 22 oprimido")
    else:
        time.sleep(2)
        print("nada en el but")

    GPIO.cleanup()