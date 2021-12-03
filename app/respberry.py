import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  #Para usar números de pin de placa y no del procesador
GPIO.setwarnings(False) #Impedir popups de warnings no importantes en este caso


led = 21
boton = 16
GPIO.setup(led, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(boton, GPIO.IN, GPIO.PUD_UP)

while True:

    if GPIO.input(led) == True:
        print("falso led oprimido")
    else:
        print("nada en el led")

    if GPIO.input(boton) == True:
        print("falso 22 oprimido")
    else:
        print("nada en el but")

GPIO.cleanup()