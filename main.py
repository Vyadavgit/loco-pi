import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime

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

# SENSORS
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
obstacle = False
last_buzz_time = datetime.now()
init_buzz = True
last_checked_interval = last_buzz_time
no_of_times_obstacle_not_detected = 0

def obstacle_detected():
    global last_buzz_time, init_buzz, obstacle, no_of_times_obstacle_not_detected, last_checked_interval
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
        if not obstacle_detected_in_last_five_checks():
            obstacle = False
    else:
        print("Object detected: YES" + ", timestamp: "+ str(datetime.now().ctime))
        # Check if 10 sec has passed since last buzz
        current_time = datetime.now()
        if (current_time - last_buzz_time).total_seconds() >= 10 or init_buzz:
            GPIO.output(buzzer, True)  # Buzz
            init_buzz = False
            sleep(.5)  # Buzz for .5 second
            GPIO.output(buzzer, False)  # Stop buzzing
        last_buzz_time = current_time  # Update last buzz time
        obstacle = True
        no_of_times_obstacle_not_detected = 0
        last_checked_interval = last_buzz_time
    return obstacle

def obstacle_detected_in_last_five_checks():
    global no_of_times_obstacle_not_detected, last_checked_interval
    margin_seconds = 5
    if ((datetime.now() - last_checked_interval).total_seconds() >= 10) and not ((datetime.now() - last_buzz_time).total_seconds() > 50+margin_seconds):
        no_of_times_obstacle_not_detected += 1
        print("No. of times obstacle not detected: "+str(no_of_times_obstacle_not_detected) + " timestamp: "+ str(last_checked_interval.ctime))
        last_checked_interval = datetime.now()
        return True
    else:
        print("Obstacle not detected for last five checks")
        return False
    
def move_forward():
    # Motor 1 forward
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(80)

    # Motor 2 forward
    GPIO.output(In4, GPIO.LOW)
    GPIO.output(In3, GPIO.HIGH)
    pwm2.ChangeDutyCycle(80)

def move_backward():
    # Motor 1 backward
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    pwm1.ChangeDutyCycle(80)

    # Motor 2 backward
    GPIO.output(In4, GPIO.HIGH)
    GPIO.output(In3, GPIO.LOW)
    pwm2.ChangeDutyCycle(80)

def stop():
    print("Stopping motors...")
    # Stop both motors
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.LOW)
    pwm1.ChangeDutyCycle(0)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.LOW)
    pwm2.ChangeDutyCycle(0)
    print("Stopped.")


running = False   
try:
    while True:
        sleep(2)
        state = GPIO.input(IR_receiverPin)
        print("IR receiver state:", "HIGH" if state else "LOW")
        obstacle_detected()
        if obstacle and no_of_times_obstacle_not_detected < 5 and running:
            print("Stopping############################################")
            # stop()
            running = False
        else:
            running = True
            print("Running.............................................")
            # move_forward()
except KeyboardInterrupt:
    print("Stopping...")
# finally:
#     GPIO.cleanup()
#     print("GPIO cleaned up. Program stopped.")


