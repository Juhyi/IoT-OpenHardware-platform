import sys
import RPi.GPIO as GPIO
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QTimer

# UI 파일 로드
ui_path = "ui/IRControl.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(ui_path)

# GPIO 설정
pirPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class IRDetectionApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("IR Detection")
        self.statusLabel.setText("IR Sensor Status: Waiting...")

        # 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_ir_status)
        self.timer.start(100)  # 0.1초마다 상태 확인

    def check_ir_status(self):
        if GPIO.input(pirPin) == GPIO.HIGH:
            self.statusLabel.setText("IR Sensor Status: Detected")
            # 감지되면 여기에 추가적인 동작을 수행할 수 있음
        else:
            self.statusLabel.setText("IR Sensor Status: Not Detected")

    def closeEvent(self, event):
        GPIO.cleanup()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = IRDetectionApp()
    mainWindow.show()
    sys.exit(app.exec_())
