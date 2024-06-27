# 媛뺤궗??肄붾뱶
import RPi.GPIO as GPIO
import time

fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [17, 26, 16, 25, 27, 4, 18]
fndSels = [20, 19, 5, 22]

#GPIO ?ㅼ젙
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
   GPIO.setup(fndSeg, GPIO.OUT)
   GPIO.output(fndSeg, 0)

for fndSel in fndSels:
   GPIO.setup(fndSel, GPIO.OUT)
   GPIO.output(fndSel, 1)

def fndOut(data, sel):	# ?レ옄 ?쒗쁽
   for i in range(0, 7):
      GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
   for j in range(0, 2):		# ?먮━?섏쓽 fnd留?on
        if j == sel:
            GPIO.output(fndSels[j], 0)
        else:
            GPIO.output(fndSels[j],1)
count = 0

try:
    while True:
        count += 1
        d1000 = count /1000
        d100 = count % 1000 / 100
        d10 = count % 100 / 10
        d1 = count % 10
        d = [d1, d10, d100, d1000]

        for i in range(0, 4):
            fndOut(int(d[i]), i)
            time.sleep(0.5)

except KeyboardInterrupt:
   GPIO.cleanup()
