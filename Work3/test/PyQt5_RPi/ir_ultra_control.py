import RPi.GPIO as GPIO
import time


IR_SENSOR_PIN = 17
TRIG_PIN = 23
ECHO_PIN = 24
BUZZER_PIN = 18

def setup_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    
    global Buzz
    Buzz = GPIO.PWM(BUZZER_PIN, 440)
    Buzz.stop()

def is_sensor_detected():
    return GPIO.input(IR_SENSOR_PIN)

def measure():
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.5)
    
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance
