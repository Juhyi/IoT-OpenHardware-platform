import RPi.GPIO as GPIO
import time

switch = 6
ledR = 21
ledB = 20
ledG = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN) 
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)

index = 0  
last_state = GPIO.input(switch) 

try:
    while True:
        current_state = GPIO.input(switch)
        if last_state == GPIO.HIGH and current_state == GPIO.LOW:  
            if index == 0:
                GPIO.output(ledR, False)
                GPIO.output(ledB, True)
                GPIO.output(ledG, True)
                index = 1
            elif index == 1:
                GPIO.output(ledR, True)
                GPIO.output(ledB, False)
                GPIO.output(ledG, True)
                index = 2
            elif index == 2:
                GPIO.output(ledR, True)
                GPIO.output(ledB, True)
                GPIO.output(ledG, False)
                index = 0
        
        last_state = current_state  
        time.sleep(0.1)  
except KeyboardInterrupt:
    GPIO.cleanup()
