import sys
import time
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
from gpio_thread import GPIOThread
import ir_control 
import RPi.GPIO as GPIO

led = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
trigPin = 27
echoPin = 17

melody = [261]
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

learn2_form_class = uic.loadUiType("ui/window2.ui")[0]

class Learn2Window(QMainWindow, learn2_form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		ir_control.setup_sensor()
		self.start_sensor_btn.clicked.connect(self.start_sensor_detection)
		self.stop_sensor_btn.clicked.connect(self.stop_sensor_detection)

		self.sensor_timer = QTimer(self)
		self.sensor_timer.timeout.connect(self.check_sensor)

		distance = ir_control.measure()
		melody = [261]
	def start_sensor_detection(self):
		self.sensor_timer.start(500)

	def stop_sensor_detection(self):
		self.sensor_timer.stop()
		self.message_label.setText("IR sensor")

	def check_sensor(self):
		if ir_control.is_sensor_detected():
			self.message_label.setText("detected now --led ON")
			GPIO.output(led, False)
		else:
			self.message_label.setText("No detected --led Off")
			GPIO.output(led, True)
	
	def check_distance(self):
		global distance, melody
		if 5 <distance <= 7:
			ir_control.Buzz.start(100)
			ir_control.Buzz.ChangeFrequency(melody[0])
			time.sleep(0.3)
			ir_control.Buzz.stop()
			self.distance_label.setText("Distancce 7 under: %.2f cm" %distance)
			time.sleep(1)
		if 3 <distance <= 5:
			ir_control.Buzz.start(100)
			ir_control.Buzz.ChangeFrequency(melody[0])
			time.sleep(0.1)
			ir_control.Buzz.stop()
			self.distance_label.setText("Distance 5 under!! : %.2f cm" %distance)
			time.sleep(1)
		if distance <= 3:
			ir_control.Buzz.start(100)
			ir_control.Buzz.ChangeFrequency(melody[0])
			time.sleep(0.001)
			ir_control.Buzz.stop()
			self.distance_label.setText("Distance 3 under!! : %.2f cm" %distance)
			time.sleep(1)
		else:
			self.distance_label.setText("Distance: %.2f cm" %distance)
