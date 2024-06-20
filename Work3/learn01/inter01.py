#interrput

import RPi.GPIO as GPIO
import time

#pin 설정
led =21
switch =8
#인터럽트 변수
intFlag = False

GPIO.setmode(GPIO.BCN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

def ledBlink(channel):
	global intFlag
		if intFlag == False:
			GPIO.output(led, True)
			intFlag = True
		else:
			GPIO.output(led, False)
			intFlag = False

# 인터럽트 설정(switch핀에 riging 신호가 잡히면 callback 함수를 실행)
GPIO.add_event_detect(switch, GPIO.FISING, callback=ledBlank)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup
