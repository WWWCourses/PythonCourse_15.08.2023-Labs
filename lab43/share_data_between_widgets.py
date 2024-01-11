from re import M
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class Form(qtw.QWidget):
	submit = qtc.pyqtSignal(str)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Login Form')
		self.center()

		mainLayout = qtw.QVBoxLayout(self)
		self.le_UserName = qtw.QLineEdit()
		self.btn_Submit =qtw.QPushButton('Submit')
		mainLayout.addWidget(self.le_UserName)
		mainLayout.addWidget(self.btn_Submit)

		self.btn_Submit.clicked.connect( self.onSubmit )

	@qtc.pyqtSlot(bool)
	def onSubmit(self):
		self.submit.emit(self.le_UserName.text())
		self.close()

	def center(self):
		 # Set window size and center it on the screen
		window_width = 400
		window_height = 400
		available_geometry = qtg.QGuiApplication.primaryScreen().availableGeometry()
		# print(f'available_geometry={available_geometry}')

		self.setGeometry(
			(available_geometry.width() - window_width) // 2,
			(available_geometry.height() - window_height) // 2,
			window_width,
			window_height
		)


class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setGeometry(300, 200, 400, 300)

		self.btnShowForm = qtw.QPushButton('Show Form')
		mainLayout = qtw.QHBoxLayout(self)
		mainLayout.addWidget(self.btnShowForm)

		self.btnShowForm.clicked.connect(self.onBtnShowForm)

	@qtc.pyqtSlot()
	def onBtnShowForm(self):
		# show Form widget
		self.form = Form()
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