import time

import RPi.GPIO as GPIO

IR_transmitter = 24
IR_receiver = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_transmitter, GPIO.OUT)
GPIO.setup(IR_receiver, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(IR_transmitter, GPIO.LOW)
print("IR initialization complete. Transmitter on pin:", IR_transmitter)

try:
    while True:
        GPIO.output(IR_transmitter, GPIO.HIGH)
        print("Emitting IR signal...")
        # time.sleep(0.1)  # Transmit for 100ms
        # GPIO.output(IR_transmitter, GPIO.LOW)
        
        if GPIO.input(IR_receiver) == GPIO.HIGH:
            print("IR signal received on pin:", IR_receiver)
        else:
            print("No IR signal detected")
        
        GPIO.output(IR_transmitter, GPIO.LOW)
        time.sleep(0.5)  # Wait for 500ms before the next transmission

except KeyboardInterrupt:
    print("Stopping...")
finally:
    GPIO.output(IR_transmitter, GPIO.LOW)
    GPIO.cleanup(IR_receiver)
    GPIO.cleanup()
    print("GPIO cleaned up. Program stopped.")
    print()
