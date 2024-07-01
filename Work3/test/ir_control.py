import sys
import time
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
import ir_ultra_control  # 적외선/초음파 센서 제어
import RPi.GPIO as GPIO

# LED 핀 설정
led = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# Melody 설정
melody = [261]

# UI 파일 로드
learn2_form_class = uic.loadUiType("ui/window2.ui")[0]

class Learn2Window(QMainWindow, learn2_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 적외선 센서 설정
        ir_ultra_control.setup_sensor()
        
        # 버튼 클릭 이벤트 연결
        self.start_sensor1_btn.clicked.connect(self.start_sensor1_detection)
        self.stop_sensor1_btn.clicked.connect(self.stop_sensor1_detection)
        self.start_sensor2_btn.clicked.connect(self.start_sensor2_detection)
        self.stop_sensor2_btn.clicked.connect(self.stop_sensor2_detection)

        # 타이머 설정
        self.sensor1_timer = QTimer(self)
        self.sensor1_timer.timeout.connect(self.check_sensor1)
        
        self.sensor2_timer = QTimer(self)
        self.sensor2_timer.timeout.connect(self.check_distance2)

        # 초기 라벨 설정
        self.message_label.setText("IR sensor")
        self.distance_label.setText("Distance: N/A")

    def start_sensor1_detection(self):
        self.sensor1_timer.start(500)

    def stop_sensor1_detection(self):
        self.sensor1_timer.stop()
        self.message_label.setText("IR sensor")

    def start_sensor2_detection(self):
        self.sensor2_timer.start(500)

    def stop_sensor2_detection(self):
        self.sensor2_timer.stop()
        self.distance_label.setText("Distance: N/A")

    def check_sensor1(self):
        if ir_ultra_control.is_sensor_detected():
            self.message_label.setText("Detected now -- LED ON")
            GPIO.output(led, True)
            self.activate_buzzer(distance=1)  # 부저 작동
        else:
            self.message_label.setText("No detected -- LED Off")
            GPIO.output(led, False)

    def check_distance2(self):
        distance = ir_ultra_control.measure()
        if distance <= 7:
            self.activate_buzzer(distance)
        self.distance_label.setText("Distance: %.2f cm" % distance)

    def activate_buzzer(self, distance):
        if 5 < distance <= 7:
            ir_ultra_control.Buzz.start(100)
            ir_ultra_control.Buzz.ChangeFrequency(melody[0])
            time.sleep(0.3)
            ir_ultra_control.Buzz.stop()
        elif 3 < distance <= 5:
            ir_ultra_control.Buzz.start(100)
            ir_ultra_control.Buzz.ChangeFrequency(melody[0])
            time.sleep(0.1)
            ir_ultra_control.Buzz.stop()
        elif distance <= 3:
            ir_ultra_control.Buzz.start(100)
            ir_ultra_control.Buzz.ChangeFrequency(melody[0])
            time.sleep(0.001)
            ir_ultra_control.Buzz.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Learn2Window()
    mainWindow.show()
    sys.exit(app.exec_())