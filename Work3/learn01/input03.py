import RPi.GPIO as GPIO
import time


led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		command = input("o:켜기, x:끄기: ")
		if command.lower() == 'o':
			GPIO.output(led, False)
			print("ON")
		elif command.lower() == 'x':
			GPIO.output(led, True)
			print("OFF")


except KeyboardInterrupt:
	GPIO.cleanup()
