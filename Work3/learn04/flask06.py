from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

led = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

@app.route('/')
def home () :
	return render_template("index.html")

@app. route('/data', methods = ['POST'])
def data():
	data = request.form['led']
	if (data == 'on' ):
		GPIO.output(led, False)
		return home()

	elif (data == 'off' ):
		GPIO.output(led, True)
		return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10015)
