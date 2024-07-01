import sys
import time
import RPi.GPIO as GPIO
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import digit_seg

window5_form_class = uic.loadUiType("ui/window5.ui")[0]

class Learn5Window(QMainWindow, window5_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.count = 0

        # 버튼 클릭 이벤트 연결
        self.increase_button.clicked.connect(self.increase_count)
        self.dial.valueChanged.connect(self.update_count)

        # 디스플레이 갱신 타이머 설정
        self.display_timer = QTimer(self)
        self.display_timer.timeout.connect(self.update_display)
        self.display_timer.start(10)

    def increase_count(self):
        self.count = (self.count + 1) % 10000
        self.lcd_number.display(self.count)

    def update_count(self):
        self.count = self.dial.value()
        self.lcd_number.display(self.count)

    def update_display(self):
        digit_seg.display_number(self.count)