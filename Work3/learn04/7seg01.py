import RPi.GPIO as GPIO
import time

segments = {
	'a' : 17, 'b':26, 'c':16, 'd':25, 'e':27, 'f':4, 'g':18
}

digits = {
	1:('b', 'c')
}

def setup():
	GPIO.setmode(GPIO.BCM)
	for segment in segments.values():
		GPIO.setup(segment, GPIO.OUT)
		GPIO.output(segment,False)

def display_digit(number):
	if number in digits:
		for segment in segments.values():
			GPIO.output(segment, False)

		for segment in digits[number]:
			GPIO.output(segments[segment], True)


try:
	setup()
	display_digit(1)
	time.sleep(5)  # 숫자 1을 5초 동안 표시

except:
    GPIO.cleanup()
