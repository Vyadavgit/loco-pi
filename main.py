import RPi.GPIO as GPIO
import time

IR_receiver = 12
IR_emitter = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_receiver, GPIO.IN)  # No pull-up or pull-down specified
GPIO.setup(IR_emitter, GPIO.OUT)  # Set IR emitter pin as output

print("Monitoring IR receiver on pin:", IR_receiver)

try:
    while True:
        state = GPIO.input(IR_receiver)
        print("IR receiver state:", "HIGH" if state else "LOW")
        
        # Control IR emitter based on receiver state
        if state:
            GPIO.output(IR_emitter, GPIO.HIGH)  # Turn on IR emitter
            print("IR emitter state: ON")
        else:
            GPIO.output(IR_emitter, GPIO.LOW)  # Turn off IR emitter
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