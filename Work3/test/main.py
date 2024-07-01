import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
import led_buzz
from gpio_thread import GPIOThread
import window1
import window2
# Main.ui 파일을 로드
main_form_class = uic.loadUiType("ui/MainWindow.ui")[0]
learn1_form_class = uic.loadUiType("ui/window1.ui")[0]
learn2_form_class = uic.loadUiType("ui/window2.ui")[0]
learn3_form_class = uic.loadUiType("ui/window3.ui")[0]
learn4_form_class = uic.loadUiType("ui/window4.ui")[0]
learn5_form_class = uic.loadUiType("ui/window5.ui")[0]
learn6_form_class = uic.loadUiType("ui/window6.ui")[0]

class MainWindow(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 서브 창을 열기 위한 버튼 클릭 이벤트와 슬롯 연결
        self.button1.clicked.connect(self.open_learn1_window)
        self.button2.clicked.connect(self.open_learn2_window)
        self.button3.clicked.connect(self.open_learn3_window)
        self.button4.clicked.connect(self.open_learn4_window)
        self.button5.clicked.connect(self.open_learn5_window)
        self.button6.clicked.connect(self.open_learn6_window)
        # ControlWindow 인스턴스 생성
        self.learn1_window = None
        self.learn2_window = None
        self.learn3_window = None
        self.learn4_window = None
        self.learn5_window = None
        self.learn6_window = None


    def open_learn1_window(self):
        if self.learn1_window is None:
            self.learn1_window = window1.Learn1Window()
        self.learn1_window.show()
    def open_learn2_window(self):
        if self.learn2_window is None:
            self.learn2_window = window2.Learn2Window()
        self.learn2_window.show()
    def open_learn3_window(self):
        if self.learn3_window is None:
            self.learn3_window = window3.Learn2Window()
        self.learn3_window.show()
    def open_learn4_window(self):
        if self.learn4_window is None:
            self.learn4_window = window4.Learn2Window()
        self.learn4_window.show()
    def open_learn5_window(self):
        if self.learn5_window is None:
            self.learn5_window = window5.Learn2Window()
        self.learn5_window.show()
    def open_learn6_window(self):
        if self.learn6_window is None:
            self.learn6_window = window6.Learn2Window()
        self.learn6_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())
