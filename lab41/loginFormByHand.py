import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# TODO: fix layouts
		# create child widgets:
		lblTitle = qtw.QLabel('Simple Login Form', parent=self)
		formLayout = qtw.QFormLayout()
		leUserName = qtw.QLineEdit()
		leUserPass = qtw.QLineEdit()
		formLayout.addRow('user name:' , leUserName)
		formLayout.addRow('user pass:' , leUserPass)

		# create main layout
		mainLayout = qtw.QVBoxLayout()
		lblLayout = qtw.QHBoxLayout()
		lblLayout.addWidget(lblTitle)
		mainLayout.addLayout(lblLayout)
		mainLayout.addLayout(formLayout)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	window = MainWindow()
	window.show()
	sys.exit(app.exec())