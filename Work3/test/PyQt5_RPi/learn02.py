#ir sensor / collision prevention
import RPi.GPIO as GPIO
import time

SENSOR_PIN = 17

def setup_sensor():
	GPIO.setup(SENSOR_PIN, GPIO.IN)

def is_sensor_detected():
	return GPIO.input(SENSOR_PIN) == GPIO.HIGH
 
