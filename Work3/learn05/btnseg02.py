import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# 세그먼트와 디스플레이 핀 설정
segPin = (17, 26, 16, 25, 27, 4, 18)
digits = (22, 5, 19, 20)
swPin = 6

oldSw=0
newSw =0
# 세그먼트와 디스플레이 핀 초기화
for i in segPin:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 0)

for i in digits:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 1)

# 숫자와 각 세그먼트 핀 매핑
segments = {
    0: (1, 1, 1, 1, 1, 1, 0, 0),
    1: (0, 1, 1, 0, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1, 0),
    3: (1, 1, 1, 1, 0, 0, 1, 0),
    4: (0, 1, 1, 0, 0, 1, 1, 0),
    5: (1, 0, 1, 1, 0, 1, 1, 0),
    6: (1, 0, 1, 1, 1, 1, 1, 0),
    7: (1, 1, 1, 0, 0, 1, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1, 0),
    9: (1, 1, 1, 1, 0, 1, 1, 0)
}

# 스위치 핀 설정
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

    for _ in range(50):  # Increase this value to make the display more stable
        display_digit(thousands, 0)
        display_digit(hundreds, 1)
        display_digit(tens, 2)
        display_digit(ones, 3)

try:
    count = 0
    while True:
    	newSw = GPIO.input(swPin)
        if newSw == 1 and oldSw ==0:
            time.sleep(0.01)
            if GPIO.input(swPin) == False:  # 스위치가 여전히 눌린 상태인지 확인
                count = (count + 1) % 10000  # 카운트를 증가시키고 9999 이후 0으로 초기화
                print("Display number:", count)
                while GPIO.input(swPin) == False:  # 버튼을 뗄 때까지 대기
                	time.sleep(0.1)
        
        display_number(count)
        time.sleep(0.005)  # 짧은 지연시간으로 디스플레이 안정화
        
        oldSw = newSw
except KeyboardInterrupt:
    GPIO.cleanup()
