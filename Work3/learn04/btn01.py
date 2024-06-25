#import RPi.GPIO as GPIO
from gpiozero import Button
import time

swPin = Button(6)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(swPin, GPIO.IN)

oldSw =0
newSw =0

try:
	while True:
		newSw = swPin.is_pressed
		if newSw != oldSw:
			oldSw = newSw

			if newSw == 1:
				print("click")

			time.sleep(0.2)

except KeyboardInterrupt:
	pass
