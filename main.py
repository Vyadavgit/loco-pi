import RPi.GPIO as GPIO
import time

IR_transmitter = 24
IR_receiver = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_transmitter, GPIO.OUT)
GPIO.setup(IR_receiver, GPIO.IN)

GPIO.output(IR_transmitter, GPIO.LOW)
print("IR initialisation.....",IR_transmitter)

try:
    while True:
        GPIO.output(IR_transmitter,GPIO.HIGH)
        print("Emitting IR...",IR_transmitter)
        if(GPIO.input(IR_receiver)):
            print("Receiving IR...",IR_receiver)
except KeyboardInterrupt:
    print("stopping...")
    GPIO.output(IR_transmitter, GPIO.LOW)
    print("Tramsmitting IR...",IR_transmitter)
    print("Receiving IR...",IR_receiver)
    print("stopped")
    