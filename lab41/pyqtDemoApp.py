from gc import enable
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	# window = qtw.QWidget(cursor=qtc.Qt.CursorShape.WaitCursor, enabled=True)
	window = qtw.QWidget()
	window.setCursor(qtc.Qt.CursorShape.WaitCursor)
	window.setEnabled(True)
	# window = MainWindow(cursor=qtc.Qt.CursorShape.WaitCursor)
	window.show()
	sys.exit(app.exec())