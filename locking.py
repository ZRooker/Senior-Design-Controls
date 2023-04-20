import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servo_pin = 4
button_pin = 26
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

pwm = GPIO.PWM(servo_pin, 50)
# pwm.start(7.5)

# pwm.ChangeDutyCycle(1)
# time.sleep(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0

if __name__ == '__main__':
    while True:
        GPIO.wait_for_edge(button_pin, GPIO.BOTH, bouncetime = 50) # Changed to wait for FALLING edge
        print("Button pressed!")
        print(state)
        state += 1 # Moved state increment up
        
        if (state % 2) == 0:
            pwm.start(7.5)
            time.sleep(.1)
            pwm.ChangeDutyCycle(7)
        else: 
            pwm.ChangeDutyCycle(6.5)
            time.sleep(.1)
            pwm.ChangeDutyCycle(0)
