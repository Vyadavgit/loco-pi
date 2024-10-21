import RPi.GPIO as GPIO
import time

buzzer = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print("Buzzer Ready.....")
GPIO.output(buzzer,True)
print("stopped")
    
