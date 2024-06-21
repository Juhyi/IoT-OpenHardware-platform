import RPi.GPIO as GPIO
import time

BUZZER_PIN = 13


FREQUENCIES = {
    '1': 262, 
    '2': 294,  
    '3': 330,  
    '4': 349,  
    '5': 392,  
    '6': 440,  
    '7': 494,  
    '8': 523   
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
buzzer = GPIO.PWM(BUZZER_PIN, 440)  

try:
    while True:
        i = input("(1~8): ")
        if i in FREQUENCIES:
            frequency = FREQUENCIES[i]
            buzzer.start(50)  
            buzzer.ChangeFrequency(frequency)
            time.sleep(0.5)  
            buzzer.stop()

except KeyboardInterrupt:
    GPIO.cleanup()
    