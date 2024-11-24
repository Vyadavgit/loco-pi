import RPi.GPIO as GPIO
import time
import datetime

# assign GPIO pins
IR_emitterPin = 24
IR_receiverPin = 25
buzzer = 23

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_emitterPin, GPIO.OUT)  # Set IR emitter pin as output
GPIO.setup(IR_receiverPin, GPIO.IN)  # No pull-up or pull-down specified
GPIO.setup(buzzer,GPIO.OUT) # set up buzzer

# initialize
GPIO.output(buzzer,False)
print("IR receiver state: ",GPIO.input(IR_receiverPin))
print("Buzzer & IRs initialized.....")

try:
    last_buzz_time = datetime.datetime.now()
    init_buzz = True
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
            # Check if 30 sec has passed since last buzz
            current_time = datetime.datetime.now()
            if (current_time - last_buzz_time).total_seconds() >= 30 or init_buzz:
                GPIO.output(buzzer, True)  # Buzz
                init_buzz = False
                # time.sleep(1)  # Buzz for 1 second
                GPIO.output(buzzer, False)  # Stop buzzing
                last_buzz_time = current_time  # Update last buzz time
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up. Program stopped.")