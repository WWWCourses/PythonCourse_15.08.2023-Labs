from re import M
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from login_form import LoginForm
from db import DB

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		db = DB()

		self.setGeometry(300, 200, 400, 300)

		self.btnShowForm = qtw.QPushButton('Login')
		mainLayout = qtw.QHBoxLayout(self)
		mainLayout.addWidget(self.btnShowForm)

		self.btnShowForm.clicked.connect(self.onBtnShowForm)

	@qtc.pyqtSlot()
	def onBtnShowForm(self):
		# show Form widget
		self.form = LoginForm()
		self.form.show()
		self.form.submit.connect(self.getUserData)


	def getUserData(self, user_name):
		user_pass = 'maria123'
		print(user_name)




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	window = MainWindow()
	window.show()
	sys.exit(app.exec())