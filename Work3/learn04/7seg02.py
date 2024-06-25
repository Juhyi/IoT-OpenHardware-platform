import RPi.GPIO as GPIO
import time

segments = {
    'a': 17, 'b': 26, 'c': 16, 'd': 25, 'e': 27, 'f': 4, 'g': 18
}

digits = {
    0: ('a', 'b', 'c', 'd', 'e', 'f'),
    1: ('b', 'c'),
    2: ('a', 'b', 'd', 'e', 'g'),
    3: ('a', 'b', 'c', 'd', 'g'),
    4: ('b', 'c', 'f', 'g'),
    5: ('a', 'c', 'd', 'f', 'g'),
    6: ('a', 'c', 'd', 'e', 'f', 'g'),
    7: ('a', 'b', 'c'),
    8: ('a', 'b', 'c', 'd', 'e', 'f', 'g'),
    9: ('a', 'b', 'c', 'd', 'f', 'g')
}

def setup():
    GPIO.setmode(GPIO.BCM)
    for segment in segments.values(): 
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, False)

def display_digit(number):
    if number in digits:
        for segment in segments.values():
            GPIO.output(segment, False)

        for segment in digits[number]:
            GPIO.output(segments[segment], True)

try:
    setup()
    while True:
        for i in range(0, 10):
            display_digit(i)
            time.sleep(1)  

except:
    GPIO.cleanup()
    