import RPi.GPIO as GPIO
from time import sleep

# init configs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor 1 (EN1, IN1, IN2)
Ena, In1, In2 = 2, 3, 4
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
pwm1 = GPIO.PWM(Ena, 100)
pwm1.start(0)

# Motor 2 (ENB, IN3, IN4)
Enb, In3, In4 = 17, 27, 22
GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)
pwm2 = GPIO.PWM(Enb, 100)
pwm2.start(0)

# IR-08H Avoid Sensor (EN_IR, OUT_IR, PWR_IR, GND_IR)
OUT_IR = 5
EN_IR = 6
GPIO.setup(OUT_IR, GPIO.IN)
GPIO.setup(EN_IR, GPIO.OUT)
print("IR Sensor Ready.....")
print(" ")

# GPIO.output(EN_IR, GPIO.HIGH)

try: 
    while True:
        GPIO.output(EN_IR, GPIO.HIGH)
        if(GPIO.input(OUT_IR)):
            print("Obstacle detected,",GPIO.input(OUT_IR))
        else:
            print("Obstacle clear,",GPIO.input(OUT_IR))
    # while GPIO.input(OUT_IR) != GPIO.HIGH:
    #     print(GPIO.input(OUT_IR))
    #     # Motor 1 forward
    #     GPIO.output(In1, GPIO.LOW)
    #     GPIO.output(In2, GPIO.HIGH)
    #     pwm1.ChangeDutyCycle(80)

    #     # Motor 2 forward
    #     GPIO.output(In4, GPIO.LOW)
    #     GPIO.output(In3, GPIO.HIGH)
    #     pwm2.ChangeDutyCycle(80)
except KeyboardInterrupt:
    print("stopped")
    # GPIO.cleanup()


    
