import RPi.GPIO as GPIO #Librería para controlar GPIO
import time #Librería para funciones relacionadas con tiempo (sleep)

GPIO.setmode(GPIO.BCM) #Simplemente nos sirve para usar números de pin de placa y no del procesador
GPIO.setwarnings(False) #Con esto impedimos que nos aparezcan warnings que en este caso no serán importantes

led = 21 #Variable donde ponemos el pin que usaremos para el LED
btn1 = 6 ##Variable donde ponemos el pin que usaremos para el pulsador
btn2 = 12 ##Variable donde ponemos el pin que usaremos para el pulsador


GPIO.setup(led, GPIO.OUT) #Configuramos el pin 21 (led) como salida
GPIO.setup(btn1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, GPIO.PUD_UP) #Configuramos el pin 13 (btn) como entrada con resistencia de pull up

while True:

    if GPIO.input(btn1) == False:
        print ("Pulsador1 está pulsado")
        tiempo = 0.1
    else:
        tiempo = 1;
    
    if GPIO.input(btn2) == False:
        print ("Pulsador2 está pulsado")
        tiempo = 0.1
    else:
        tiempo = 1;

    time.sleep(tiempo) #Esperamos un tiempo para que se vea el parpadeo del LED
    
    GPIO.output(led,1) #Encendemos el LED

    time.sleep(tiempo) #Esperamos un tiempo para que se vea el parpadeo del LED

    GPIO.output(led,0) #Apagamos el LED

GPIO.cleanup()