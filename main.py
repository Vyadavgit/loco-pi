import RPi.GPIO as GPIO
from time import sleep

# init configs
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# IR-08H Avoid Sensor (EN_IR, OUT_IR, PWR_IR, GND_IR)
OUT_IR = 16
EN_IR = 18
GPIO.setup(OUT_IR, GPIO.IN)
GPIO.setup(EN_IR, GPIO.OUT)
# GPIO.output(EN_IR, GPIO.HIGH)
print("IR Sensor Ready.....")
print(" ")

# GPIO.output(EN_IR, GPIO.HIGH)

try: 
    while True:
        # print("enable pin: ",GPIO.input(EN_IR))
        if(GPIO.input(OUT_IR)):
            print("Obstacle detected")
        else:
            print("Obstacle clear")
except KeyboardInterrupt:
    print("stopped")


    
