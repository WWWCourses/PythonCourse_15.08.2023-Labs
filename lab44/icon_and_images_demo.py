import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create widgets
		self.main_label = qtw.QLabel('Main Window Components')
		self.img_label = qtw.QLabel()

		# load image from given path
		pixmap = qtg.QPixmap('./images/calculator.png')

		# set image to label
		self.img_label.setPixmap(pixmap)

		# Optional, resize label to image size
		self.img_label.resize(pixmap.width(),
						  pixmap.height())

		self.main_layout = qtw.QVBoxLayout(self)
		self.main_layout.addWidget(self.main_label)
		self.main_layout.addWidget(self.img_label)

		self.setWindowTitle('Image test')
		self.setWindowIcon(qtg.QIcon('./images/calculator.png'))
		self.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())