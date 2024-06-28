import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
import led_control
from gpio_thread import GPIOThread

# Main.ui 파일을 로드
main_form_class = uic.loadUiType("ui/MainWindow.ui")[0]
control_form_class = uic.loadUiType("ui/ControlWindow.ui")[0]
ir_form_class = uic.loadUiType("ui/IRControl.ui")[0]

class ControlWindow(QMainWindow, control_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 초기 설정
        led_control.setup()

        # 버튼 클릭 이벤트와 슬롯 연결
        self.btnledcolor.clicked.connect(self.change_color)

        # LED 상태 레이블 초기화
        self.update_led_status()

        # GPIO 스레드 시작
        self.gpio_thread = GPIOThread(self.change_color)
        self.gpio_thread.start()

        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.statusLabel.setFont(font)

    def change_color(self):
        led_control.change_led_color()
        # LED 색상 업데이트
        self.update_led_status()

    def update_led_status(self):
        if led_control.current_index == 0:
            self.statusLabel.setText("Current LED: Green")
        elif led_control.current_index == 1:
            self.statusLabel.setText("Current LED: Red")
        elif led_control.current_index == 2:
            self.statusLabel.setText("Current LED: Blue")

    def closeEvent(self, event):
        self.gpio_thread.stop()
        self.gpio_thread.join()
        led_control.cleanup()
        event.accept()

class IRControl(QMainWindow, ir_form_class):
		def __init__(self):
			super().__init__()
			self.setupUi(self)		

			font = QFont()
			font.setPointSize(20)  # 글꼴 크기 설정
			font.setBold(True)     # 글꼴 두께 설정
			self.statusLabel.setFont(font)


class MainWindow(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 서브 창을 열기 위한 버튼 클릭 이벤트와 슬롯 연결
        self.button1.clicked.connect(self.open_control_window)
        self.button2.clicked.connect(self.open_IR_window)
        # ControlWindow 인스턴스 생성
        self.control_window = None
        self.ir_window = None
    def open_control_window(self):
        if self.control_window is None:
            self.control_window = ControlWindow()
        self.control_window.show()

    def open_IR_window(self):
    		if self.ir_window is None:
    				self.ir_window = IRControl()
    		self.ir_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
