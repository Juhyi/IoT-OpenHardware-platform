import sys
import time
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import datetime

# UI 파일 로드
learn4_form_class = uic.loadUiType("ui/window4.ui")[0]

SWITCH_PIN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
class Learn4Window(QMainWindow, learn4_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼 클릭 이벤트 연결
        self.capture_button.clicked.connect(self.capture_image)

        # Picamera2 설정
        self.picam2 = Picamera2()
        camera_config = self.picam2.create_preview_configuration()
        self.picam2.configure(camera_config)
        self.picam2.start()
        time.sleep(2)
        

        self.capture1_button.clicked.connect(self.capture_realtime_image)
        # self.switch_button.clicked.connect(self.toggle_switch_monitoring)

        # 스위치 모니터링 타이머 설정
        self.switch_timer = QTimer(self)
        self.switch_timer.timeout.connect(self.check_switch)
        self.monitoring = False

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.status_label.setFont(font)
        self.status1_label.setFont(font)

    def capture_image(self):
        self.picam2.capture_file("test_image.jpg")
        self.status_label.setText("[test_image.jpg] 파일명으로 사진 저장 성공!")

    def capture_realtime_image(self):
        now = datetime.datetime.now()
        fileName = now.strftime('%Y-%m-%d %H:%M:%S')
        self.picam2.capture_file(fileName + '.jpg')
        self.status1_label.setText(f"[{fileName}.jpg] 실시간 사진 촬영 성공")

    def toggle_switch_monitoring(self):
        if self.monitoring:
            self.switch_timer.stop()
            self.monitoring = False
            self.switch_button.setText("Start Monitoring")
            self.status1_label.setText("Switch monitoring stopped.")
        else:
            self.switch_timer.start(100)
            self.monitoring = True
            self.switch_button.setText("Stop Monitoring")
            self.status1_label.setText("Switch monitoring started.")

    def check_switch(self):
        if GPIO.input(SWITCH_PIN) == GPIO.HIGH:
            now = datetime.datetime.now()
            fileName = now.strftime('%Y-%m-%d %H:%M:%S')
            self.picam2.capture_file(fileName + '.jpg')
            self.status1_label.setText(f"[{fileName}.jpg] 실시간 사진 촬영 성공")
            time.sleep(0.2)