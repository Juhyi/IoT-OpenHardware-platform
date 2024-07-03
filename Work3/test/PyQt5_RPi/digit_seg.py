import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

segPin = (17, 26, 16, 25, 27, 4, 18)
digits = (22, 5, 19, 20)
swPin = 6

GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for i in segPin:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 0)

for i in digits:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 1)

# 숫자와 각 세그먼트 핀 매핑
segments = {
    0: (1, 1, 1, 1, 1, 1, 0),
    1: (0, 1, 1, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1),
    3: (1, 1, 1, 1, 0, 0, 1),
    4: (0, 1, 1, 0, 0, 1, 1),
    5: (1, 0, 1, 1, 0, 1, 1),
    6: (1, 0, 1, 1, 1, 1, 1),
    7: (1, 1, 1, 0, 0, 1, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 1)
}

def display_digit(number, digit_index):
    for loop in range(7):
        GPIO.output(segPin[loop], segments[number][loop])
    GPIO.output(digits[digit_index], 0)
    time.sleep(0.005)
    GPIO.output(digits[digit_index], 1)

def display_number(number):
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10

    display_digit(thousands, 0)
    display_digit(hundreds, 1)
    display_digit(tens, 2)
    display_digit(ones, 3)