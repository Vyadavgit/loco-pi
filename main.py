import RPi.GPIO as GPIO
import time

IR_emitterPin = 24
IR_receiverPin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_emitterPin, GPIO.OUT)  # Set IR emitter pin as output
GPIO.setup(IR_receiverPin, GPIO.IN)  # No pull-up or pull-down specified

print("Monitoring IR receiver on pin:", IR_receiverPin)

try:
    while True:
        state = GPIO.input(IR_receiverPin)
        print("IR receiver state:", "HIGH" if state else "LOW")
        
        # Control IR emitter based on receiver state
        if state:
            GPIO.output(IR_emitterPin, GPIO.HIGH)  # Turn on IR emitter
            print("IR emitter state: ON")
        else:
            GPIO.output(IR_emitterPin, GPIO.LOW)  # Turn off IR emitter
            print("IR emitter state: OFF")
        
        # Detect object based on receiver state
        if state:
            print("Object detected: NO")
        else:
            print("Object detected: YES")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up. Program stopped.")