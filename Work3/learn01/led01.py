import RPi.GPIO as GPIO

led =21

#GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BGM)
#GPIO 핀설정 (입력 /출력)
GPIO.setup(led, GPIO.OUT)

try:
	while  True:
		GPIO.outpin(led, False)

except KeyboardInterrupt: #Ctnrl + c
	GPIO.cleanup()
