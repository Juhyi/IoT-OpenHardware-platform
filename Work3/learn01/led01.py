import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)
led =6

#GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)
#GPIO 핀설정 (입력 /출력)
GPIO.setup(led, GPIO.OUT)


@app.route("/")
def led_on():
	GPIO.output(led, False)
	return "led"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="10011", debug=True)
