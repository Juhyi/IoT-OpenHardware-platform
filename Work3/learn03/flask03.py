from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
led = 6  

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

@app.route("/led")
def led_status():
    return "LED Control page"

@app.route("/led/on")
def on():
    GPIO.output(led, False)  00000000000000000000000000F
    return "<h1> LED ON!</h1>"
000000000000000000000000000000000000000000000000000000000000000000
@app.route("/led/off")
def off():000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    GPIO.output(led, True)  
    return "<h1> LED OFF!</h1>"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=10011, debug=True)
    finally:
        GPIO.cleanup() 