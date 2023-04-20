#Unlocking the Pi

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servo_pin = 4
button_pin = 26
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(7.5)

pwm.ChangeDutyCycle(7.5)
time.sleep(.1)

#  pwm.ChangeDutyCycle(0)
#             state = 1
#             continue
#         elif state == 1: 
#             pwm.ChangeDutyCycle(7.5)
#             time.sleep(0.1)
#             pwm.ChangeDutyCycle(0)
#             state = 0
