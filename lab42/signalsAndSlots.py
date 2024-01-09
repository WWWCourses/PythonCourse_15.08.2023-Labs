import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		btnClose = qtw.QPushButton('Close')
		btnFoo = qtw.QPushButton('Foo')

		# qtw.QVBoxLayout(self).addWidget(btnClose)
		mainLayout = qtw.QVBoxLayout()
		mainLayout.addWidget(btnClose)
		self.setLayout(mainLayout)
		self.setGeometry(300, 300, 400, 300)

		# on btnFoo click => btnClose.close()

		# TODO: why not emitting clicked...
		btnClose.click()

		# on btnClose click => onBtnCloseClick
		btnClose.clicked.connect( self.onBtnCloseClick )

		# on btnClose press down => print('btnClose was press down')
		btnClose.pressed.connect( self.onBtnClosePress )

	def onBtnCloseClick(self):
		# close main widget:
		print('btnClose was clicked!')
		self.close()

	def onBtnClosePress(self):
		print('btnClose was press')




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	window = MainWindow()
	window.show()
	sys.exit(app.exec())