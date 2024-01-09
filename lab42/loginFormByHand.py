from lib2to3.fixes.fix_print import parend_expr
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create child widgets:
		lblTitle = qtw.QLabel('Simple Login Form')
		leUserName = qtw.QLineEdit()
		leUserPass = qtw.QLineEdit()
		leUserPass.setEchoMode(qtw.QLineEdit.EchoMode.Password)

		btnLogin = qtw.QPushButton('Login')
		btnCancel = qtw.QPushButton('Cancel')

		# create buttons layout
		buttonsLayout = qtw.QHBoxLayout()
		buttonsLayout.addWidget(btnLogin)
		buttonsLayout.addSpacing(60)
		buttonsLayout.addWidget(btnCancel)

		# create form layout
		formLayout = qtw.QFormLayout()
		formLayout.addRow('user name:' , leUserName)
		formLayout.addRow('user pass:' , leUserPass)
		formLayout.addRow('', buttonsLayout)

		# create label layout
		lblLayout = qtw.QHBoxLayout()
		lblLayout.addWidget(lblTitle)

		# create main layout
		mainLayout = qtw.QVBoxLayout(self)
		mainLayout.addLayout(lblLayout, stretch=1)
		mainLayout.setAlignment(lblLayout, qtc.Qt.AlignmentFlag.AlignCenter)
		# mainLayout.addSpacing(100)
		# mainLayout.setStretch(0 1)
		# mainLayout.setStretch(1, 3)
		mainLayout.addLayout(formLayout, stretch=3)

		self.setGeometry(300, 200, 400, 300)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	window = MainWindow()
	window.show()
	sys.exit(app.exec())