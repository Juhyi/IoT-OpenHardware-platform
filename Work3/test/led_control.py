# led_control.py
import RPi.GPIO as GPIO

LED_PINS = [20, 21, 19]  
current_index = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)
    update_led()

def change_led_color():
    global current_index
    current_index = (current_index + 1) % len(LED_PINS)
    update_led()

def update_led():
    for i, pin in enumerate(LED_PINS):
        GPIO.output(pin, i == current_index)

def cleanup():
    GPIO.cleanup()
