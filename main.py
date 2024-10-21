import RPi.GPIO as GPIO
import time

buzzer = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print("Buzzer Ready.....")

try:
    while True:
        print("buzzing...")
        GPIO.output(buzzer,True)
except KeyboardInterrupt:
    print("stopping...")
    GPIO.output(buzzer, False)
    print("stopped")
    
