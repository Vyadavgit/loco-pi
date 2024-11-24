import RPi.GPIO as GPIO
import time

IR_receiver = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_receiver, GPIO.IN)  # No pull-up or pull-down specified

print("Monitoring IR receiver on pin:", IR_receiver)

try:
    while True:
        state = GPIO.input(IR_receiver)
        print("IR receiver state:", "HIGH" if state else "LOW")
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up. Program stopped.")