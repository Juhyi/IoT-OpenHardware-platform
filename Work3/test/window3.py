import sys
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import stepper_control  # 스텝 모터 제어
import RPi.GPIO as GPIO

# LED 핀 설정
led = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# UI 파일 로드
learn3_form_class = uic.loadUiType("ui/window3.ui")[0]

class Learn3Window(QMainWindow, learn3_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 스텝 모터 설정
        stepper_control.setup_motor()

        # 버튼 클릭 이벤트 연결
        self.start_motor_btn.clicked.connect(self.start_motor)
        self.stop_motor_btn.clicked.connect(self.stop_motor)

        # 타이머 설정
        self.motor_timer = QTimer(self)
        self.motor_timer.timeout.connect(self.update_angle)

        # 초기 라벨 설정
        self.angle_label.setText("Angle: 0°")

        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.angle_label.setFont(font)
        

    def start_motor(self):
        stepper_control.start_motor()
        self.motor_timer.start(100)
        GPIO.output(led, True)
        self.angle_label.setText("Motor started")

    def stop_motor(self):
        stepper_control.stop_motor()
        self.motor_timer.stop()
        GPIO.output(led, False)
        self.angle_label.setText("Motor stopped")

    def update_angle(self):
        angle = stepper_control.get_angle()
        self.angle_label.setText(f"Angle: {angle}°")

    def closeEvent(self, event):
        stepper_control.cleanup()
        event.accept()


