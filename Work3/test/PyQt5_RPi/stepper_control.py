import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
steps = [21, 22, 23, 24]
steps_per_revolution = 2048  # 한 바퀴 회전에 필요한 스텝 수 (28BYJ-48 스텝 모터 기준)

# 스텝 순서 (반시계 방향)
step_seq = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]

# 초기화 변수
current_angle = 0
running = False

def setup_motor():
    GPIO.setmode(GPIO.BCM)
    for stepPin in steps:
        GPIO.setup(stepPin, GPIO.OUT)
        GPIO.output(stepPin, 0)

def start_motor():
    global running
    if not running:
        running = True
        _rotate_motor()

def stop_motor():
    global running
    running = False

def get_angle():
    return current_angle % 360  # 현재 각도를 360도로 나눈 나머지 값

def _rotate_motor():
    global current_angle
    while running:
        for seq in step_seq:
            for pin in range(4):
                GPIO.output(steps[pin], seq[pin])
            time.sleep(0.01)
        current_angle += (360 / steps_per_revolution)

def cleanup():
    GPIO.cleanup()
