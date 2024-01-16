import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Icons Demo')

		### use standard icon:
		standardIcon = self.style().standardIcon(getattr(qtw.QStyle.StandardPixmap,'SP_DialogYesButton'))
		self.btnStandardIcon = qtw.QPushButton('btnStandardIcon')
		self.btnStandardIcon.setIcon(standardIcon)

		### use icon from theme:
		# https://specifications.freedesktop.org/icon-naming-spec/latest/ar01s04.html
		themeIcon = qtg.QIcon.fromTheme("accessories-calculator")
		self.btnThemeIcon = qtw.QPushButton('btnThemeIcon')
		self.btnThemeIcon.setIcon(themeIcon)

		### use custom icon:
		customIcon = qtg.QIcon('./icons/submit_icon.png')
		self.btnCustomIcon = qtw.QPushButton('btnCustomIcon')
		self.btnCustomIcon.setIcon(customIcon)

		mainLayout = qtw.QVBoxLayout(self)
		mainLayout.addWidget(self.btnCustomIcon)
		mainLayout.addWidget(self.btnStandardIcon)
		mainLayout.addWidget(self.btnThemeIcon)




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	window.show()

	sys.exit(app.exec())
