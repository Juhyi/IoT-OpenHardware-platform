import RPi.GPIO as GPIO
import time

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


try:
    while True:
        distance = measure()
        if 5 <distance <= 7:
            Buzz.start(100)
            Buzz.ChangeFrequency(melody[0])
            time.sleep(0.3)
            Buzz.stop()
            print("Distancce 7 under: %.2f cm" %distance)
            time.sleep(1)
        if 3 <distance <= 5:
            Buzz.start(100)
            Buzz.ChangeFrequency(melody[0])
            time.sleep(0.1)
            Buzz.stop()
            print("Distance 5 under!! : %.2f cm" %distance)
            time.sleep(1)
        if distance <= 3:
            Buzz.start(100)
            Buzz.ChangeFrequency(melody[0])
            time.sleep(0.001)
            Buzz.stop()
            print("Distance 3 under!! : %.2f cm" %distance)
            time.sleep(1)
        else:
            print("Distance: %.2f cm" %distance)

except KeyboardInterrupt:
    GPIO.cleanup()
