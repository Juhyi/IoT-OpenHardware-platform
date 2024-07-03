import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
import led_buzz
from gpio_thread import GPIOThread

learn1_form_class = uic.loadUiType("ui/window1.ui")[0]

class Learn1Window(QMainWindow, learn1_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        led_buzz.setup()

        self.btnledcolor.clicked.connect(self.change_color)

        self.start1_btn.clicked.connect(self.start_timer)
        self.stop1_btn.clicked.connect(self.stop_timer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_auto_color)

        self.start2_btn.clicked.connect(self.switch)

        self.start3_btn.clicked.connect(self.play_sound)
        self.stop3_btn.clicked.connect(self.stop_timer)

        self.do_btn.clicked.connect(lambda: led_buzz.play_note_by_index(0))
        self.re_btn.clicked.connect(lambda: led_buzz.play_note_by_index(1))
        self.mi_btn.clicked.connect(lambda: led_buzz.play_note_by_index(2))
        self.fa_btn.clicked.connect(lambda: led_buzz.play_note_by_index(3))
        self.sol_btn.clicked.connect(lambda: led_buzz.play_note_by_index(4))
        self.la_btn.clicked.connect(lambda: led_buzz.play_note_by_index(5))
        self.si_btn.clicked.connect(lambda: led_buzz.play_note_by_index(6))
        self.high_do_btn.clicked.connect(lambda: led_buzz.play_note_by_index(7))

#        self.scale_thread = Qthread()
        self.update_led_status()

        self.gpio_thread = GPIOThread(self.change_color)
        self.gpio_thread.start()

        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.statusLabel.setFont(font)
        self.statusLabel_1.setFont(font)
        self.statusLabel_2.setFont(font)
    def change_color(self):
        led_buzz.change_led_color()
        self.update_led_status()

    def change_auto_color(self):
        led_buzz.change_led_color()
        self.update_autoled_status()

    def update_led_status(self):
        if led_buzz.current_index == 0:
            self.statusLabel.setText("Red LED ON")
        elif led_buzz.current_index == 1:
            self.statusLabel.setText("Blue LED ON")
        elif led_buzz.current_index == 2:
            self.statusLabel.setText("Green LED ON")

    def update_autoled_status(self):
        if led_buzz.current_index == 0:
            self.statusLabel_1.setText("Blue LED")
        elif led_buzz.current_index == 1:
            self.statusLabel_1.setText("Red LED")
        elif led_buzz.current_index == 2:
            self.statusLabel_1.setText("Green LED")

    def switch(self):
        self.statusLabel_2.setText("Button push")

    def play_sound(self):
        led_buzz.play_scale()

    def closeEvent(self, event):
        self.gpio_thread.stop()
        self.gpio_thread.join()
        led_buzz.cleanup()
        event.accept()

    def start_timer(self):
        self.timer.start(1000)
    def stop_timer(self):
        self.timer.stop()

    def start_autoled_timer(self):
        self.timer.start(1000)
    def stop_autoled_timer(self):
        self.timer.stop()
