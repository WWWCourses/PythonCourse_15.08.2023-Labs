import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
	# cretate custom signal which will cary a string data type data:
	sig_submit = qtc.pyqtSignal(str)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		mainLayout = qtw.QVBoxLayout(self)
		self.le_UserName = qtw.QLineEdit()

		btn_GetUserName =qtw.QPushButton('Get user name')

		mainLayout.addWidget(self.le_UserName)
		mainLayout.addWidget(btn_GetUserName)

		btn_GetUserName.clicked.connect( self.onSubmit )


	@qtc.pyqtSlot(bool)
	def onSubmit(self):
		user_name = self.le_UserName.text()
		self.sig_submit.emit( user_name )
		self.close()

	def slot1(self, x):
		print(f'slot1 is called: x = {x}')
		print(self.le_UserName.text())

	@qtc.pyqtSlot(str)
	def slot2(self, *args):
		print(f'slot2 is called wit args: {args}')



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	window = MainWindow()
	window.setGeometry(300, 300, 400, 300)
	window.show()
	sys.exit(app.exec())