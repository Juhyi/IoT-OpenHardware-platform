import RPi.GPIO as GPIO
import time

pirPin = 4
led = 19

GPIO.setmode(GPIO.BCM)
GPIO.setop(pirPin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		if GPIO.input(pirPin) == True:
	  	GPIO.output(led, False)
	  	print("detected -- led ON")
	  elif GPI.input(pirPin) == False:
	  	GPIO.output(led, True)
	  	print("No detected -- led OFF")

except KeyboardInterrupt:
	GPIO.cleanup()
