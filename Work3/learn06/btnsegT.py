import RPi.GPIO as GPIO
import time

# 0~9까지 1byte hex값
fndDatas = [0x3f, 0x06, 0x5d, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
# a~g led pin
fndSegs = [17, 26, 16, 25, 27, 4, 18]
# fnd pin
fndSels = [22, 5, 19, 20]

GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data):	# 하나의 숫자 형태를 만드는 함수
	for i in range(7):
		GPIO.output(fndSegs[i],fndDatas[data]& (0x00 << i)) 

try:
	while True:
		for i in range(4):
			GPIO.output(fndSels[i], 0) # FND 선택
		for j in  range(10):
			fndOut(5)
			time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
