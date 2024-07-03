import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import RPi.GPIO as GPIO
import time
from PyQt5 import uic

steps = [17, 18, 27, 22]  


GPIO.setmode(GPIO.BCM)
for stepPin in steps:
    GPIO.setup(stepPin, GPIO.OUT)
    GPIO.output(stepPin, 0)


step_seq = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]

current_angle = 0.0
step_angle = 5.625 / 64  # 28BYJ-48 
learn3_form_class = uic.loadUiType("ui/window3.ui")[0]

class Learn3Window(QMainWindow, learn3_form_class):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stepper Motor Controller")

        self.button = QPushButton("Start Motor")
        self.button.clicked.connect(self.start_motor)

        self.angle_label = QLabel("Current Anggle: 0.00")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.angle_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_motor)

    def start_motor(self):
        self.timer.start(100)

    def update_motor(self):
        global current_angle

        for seq in step_seq:
            for pin in range(4):
                GPIO.output(steps[pin], seq[pin])
            time.sleep(0.01)

            current_angle += step_angle
            self.angle_label.setText(f"Current Anggle: {current_angle:.2f}")

    def closeEvent(self, event):
        self.timer.stop()
        GPIO.cleanup()
        event.accept()

