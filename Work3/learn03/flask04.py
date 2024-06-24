from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
led = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

@app.route("/")
def hello():
    return "LED 제어: /led/on, /led/off, /led/clear"

@app.route("/led/<state>")
def control_led(state):
    if state == "on":
        GPIO.output(led, True)
        return "LED ON"
    elif state == "off":
        GPIO.output(led, False)
        return "LED OFF"
    elif state == "clear":
        GPIO.cleanup()
        return "GPIO Cleanup()"
    else:
        return "Invalid command"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10011, debug=True)
