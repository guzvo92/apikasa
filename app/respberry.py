import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  #Para usar números de pin de placa y no del procesador
GPIO.setwarnings(False) #Impedir popups de warnings no importantes en este caso

GPIO.setup(18, GPIO.IN, GPIO.PUD_UP) #Config pin-5(btn) como entrada con resistencia de pull up
GPIO.setup(24, GPIO.IN, GPIO.PUD_UP) #Config pin-5(btn) como entrada con resistencia de pull up
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP) #Config pin-5(btn) como entrada con resistencia de pull up

GPIO.setup(27, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)

while True:

    if GPIO.input(27) == True:
        print("falso 27 oprimido")

    if GPIO.input(22) == True:
        print("falso 22 oprimido")

