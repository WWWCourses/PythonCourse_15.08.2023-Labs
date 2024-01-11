from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class LoginForm(qtw.QWidget):
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
