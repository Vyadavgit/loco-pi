from time import sleep

import RPi.GPIO as GPIO

# init configs
GPIO.setmode(GPIO.BCM)

# IR-08H Avoid Sensor (EN_IR, OUT_IR, PWR_IR, GND_IR)
OUT_IR = 6
EN_IR = 13
GPIO.setup(OUT_IR, GPIO.IN)
GPIO.setup(EN_IR, GPIO.OUT)

# # LED (GPIO_LED)
# GPIO_LED = 12
# GPIO.setup(GPIO_LED, GPIO.OUT)

print("IR Sensor Ready.....")
print(" ")

try: 
    while True:
        if GPIO.input(OUT_IR):
            print("Obstacle detected")
            # GPIO.output(GPIO_LED, GPIO.HIGH)  # Turn on the LED
        else:
            print("Obstacle clear")
            # GPIO.output(GPIO_LED, GPIO.LOW)  # Turn off the LED
        sleep(0.2)  # Delay for stability
except KeyboardInterrupt:
    print("stopped")
# finally:
#     GPIO.cleanup()  # Clean up GPIO pins


    
