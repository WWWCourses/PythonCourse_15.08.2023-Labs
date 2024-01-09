import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		btnClose = qtw.QPushButton('Close')
		btnClick = qtw.QPushButton('Click')

		# qtw.QVBoxLayout(self).addWidget(btnClose)
		mainLayout = qtw.QVBoxLayout()
		mainLayout.addWidget(btnClose)
		mainLayout.addWidget(btnClick)
		self.setLayout(mainLayout)
		self.setGeometry(300, 300, 400, 300)


		# on btnClose click => close()
		btnClose.clicked.connect( self.close )
		# on btnClose press down => print('btnClose was press down')
		btnClose.pressed.connect( self.onBtnClosePress )

		# on btnClick => 'hi'
		btnClick.clicked.connect( self.onBtnClickClick )

	def onBtnClickClick(self):
		print('Hi...')

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