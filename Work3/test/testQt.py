from PyQt5.QtWidgets import*
from PyQt5 import uic
import sys

#form_class = uic.loadUiType("./Main.ui")[0]

class WindowClass(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui =uic.loadUi("./Main.ui",self)

		self.pushButton.clicked.connect(self.second)
		self.show()

		self.btn_1.clicked.connect(self.btn1Function)

	def b
class second(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = uic.loadUi("learn01.ui",self)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	Window = WindowClass()
	Window.show()
	app.exec_()
