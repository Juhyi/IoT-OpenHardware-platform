import RPi.GPIO as GPIO
import time

SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)

def setup_sensor():
    GPIO.setup(SENSOR_PIN, GPIO.IN)

def is_sensor_detected():
    return GPIO.input(SENSOR_PIN) == GPIO.HIGH

def measure():
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    start = time.time()

    while GPIO.input(echoPin) == False:
        start =time.time()
    while GPIO.input(echoPin) == True:
        stop = time.time()
    dlapsed = stop - start
    distance = (dlapsed * 19000) / 2

    return distance 


trigPin = 27
echoPin = 17
BUZZER_PIN = 13
melody = [261]
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
Buzz = GPIO.PWM(BUZZER_PIN, 440)
