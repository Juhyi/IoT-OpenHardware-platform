from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
import logging

app = Flask(__name__)

# �α� ����
logging.basicConfig(level=logging.DEBUG)

led = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data', methods=['POST'])
def data():
    try:
        data = request.form.get('led')
        logging.debug('Received data: %s', data)
        
        if data is None:
            logging.error('No data provided')
            return jsonify({'error': 'No data provided'}), 400
        
        if data == 'on':
            GPIO.output(led, False)
        elif data == 'off':
            GPIO.output(led, True)
        else:
            logging.error('Invalid data: %s', data)
            return jsonify({'error': 'Invalid data'}), 400
        
        return home()
    except Exception as e:
        logging.exception('An error occurred')
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10015)