# gpio_thread.py
import threading
import time
import RPi.GPIO as GPIO
import led_control

SWITCH_PIN = 6

class GPIOThread(threading.Thread):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.running = False
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def run(self):
        while self.running:
            if GPIO.input(SWITCH_PIN) == GPIO.LOW:  # 스위치 눌림 감지
                self.callback()
                time.sleep(0.2)  # 디바운싱을 위해 잠시 대기

    def stop(self):
        self.running = True
