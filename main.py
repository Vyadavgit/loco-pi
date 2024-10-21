import RPi.GPIO as GPIO
from time import sleep

# init configs
GPIO.setmode(GPIO.BCM)

# IR-08H Avoid Sensor (EN_IR, OUT_IR, PWR_IR, GND_IR)
OUT_IR = 6
EN_IR = 13
GPIO.setup(OUT_IR, GPIO.IN)
GPIO.setup(EN_IR, GPIO.OUT)
print("IR Sensor Ready.....")
print(" ")

try: 
    while True:
        if(GPIO.input(OUT_IR)):
            print("Obstacle detected")
        else:
            print("Obstacle clear")
except KeyboardInterrupt:
    print("stopped")


    
