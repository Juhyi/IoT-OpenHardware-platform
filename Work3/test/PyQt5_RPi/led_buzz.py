# led_control.py
import RPi.GPIO as GPIO
import time

LED_PINS = [20, 21, 19]
BUZZER_PIN = 18
current_index = 0

NOTES = [261, 293, 329, 349, 392, 440, 493, 523]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, True)  # 초기에는 모든 LED를 끔
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    update_led()

def change_led_color():
    global current_index
    current_index = (current_index + 1) % len(LED_PINS)  # 0, 1, 2를 순환하도록 수정
    update_led()


def update_led():
    # 모든 LED를 끔
    GPIO.output(LED_PINS[0], True)
    GPIO.output(LED_PINS[1], True)
    GPIO.output(LED_PINS[2], True)
    # 현재 선택된 LED만 켬
    GPIO.output(LED_PINS[current_index], False)

def play_note_by_index(index, duration=0.5):
    note = NOTES[index]
    p = GPIO.PWM(BUZZER_PIN, note)
    p.start(50)  # 50% 듀티 사이클
    time.sleep(duration)
    p.stop()

def play_scale():
	for note in NOTES:
		p = GPIO.PWM(BUZZER_PIN, note)
		p.start(50)  # 50% 듀티 사이클
		time.sleep(0.5)
		p.stop()


def cleanup():
    GPIO.cleanup()

