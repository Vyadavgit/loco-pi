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

def buzz():
    GPIO.output(buzzer, True)  # Buzz
    sleep(.5)  # Buzz for .5 second
    GPIO.output(buzzer, False)  # Stop buzzing

def obstacle_detected():
    obstacle = False
    states = []
    for i in range(5):
        GPIO.output(IR_emitterPin, GPIO.HIGH)
        state = GPIO.input(IR_receiverPin)
        states.append(state)
        sleep(0.1)  # Add a small delay between each reading
    state = min(states)
    print('\n')
    print('IR receiver state:', "HIGH" if state else "LOW")
    if state: # if state is HIGH means, there is no obstacle. Continue emitting IR signals
        # GPIO.output(IR_emitterPin, GPIO.HIGH)  # Turn on IR emitter
        # print("IR emitter state: ON")
        obstacle = False
    else: # if the state fluctuated, stop emitting
        # GPIO.output(IR_emitterPin, GPIO.LOW)  # Turn off IR emitter
        # print("IR emitter state: OFF")
        obstacle = True
        buzz()
    return obstacle

def obstacle_detected_during_stop():
    init_timestamp = datetime.now()
    loop_count = 0
    obstacle_detected_count = 0
    while (datetime.now() - init_timestamp).total_seconds() < 10:
        # sleep(.5)
        if(obstacle_detected()):
            obstacle_detected_count += 1
        loop_count += 1
        print('Detection ratio: '+str(obstacle_detected_count)+'/'+str(loop_count))
    detection_flag = obstacle_detected_count > 0 # if obstacle detected more than 1 time in last 10secs
    if detection_flag:
        buzz()
    return detection_flag
    
def move_forward():
    # Motor 1 forward
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(60)

    # Motor 2 forward
    GPIO.output(In4, GPIO.LOW)
    GPIO.output(In3, GPIO.HIGH)
    pwm2.ChangeDutyCycle(60)

def move_backward():
    # Motor 1 backward
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    pwm1.ChangeDutyCycle(60)

    # Motor 2 backward
    GPIO.output(In4, GPIO.HIGH)
    GPIO.output(In3, GPIO.LOW)
    pwm2.ChangeDutyCycle(60)

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

def main():
    try:
        while True:
            sleep(1)
            if not obstacle_detected():
                move_forward()
                print("Running.............................................")
            else:
                stop()
                print("!!...Stoped. Obstacle avoidance activated...!!")
                while obstacle_detected_during_stop():
                    print('\nOBSTACLE DETECTED. Rescan for next 10 seconds...')
    except KeyboardInterrupt:
        print("Stopping...")
    # finally:
    #     GPIO.cleanup()
    #     print("GPIO cleaned up. Program stopped.")

if __name__ == "__main__":
    main()