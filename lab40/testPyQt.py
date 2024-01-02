from email.charset import QP
import sys

from PyQt6.QtWidgets import QApplication,QWidget, QPushButton, QMainWindow

from PyQt6.QtCore import QRect

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt6 App Works')

window.menuBar().addMenu('File')

btnOK = QPushButton('OK',parent=window)
btnCancel = QPushButton('Cancel',parent=window)

btnOK.setGeometry(QRect(50, 100, 200, 50))
btnCancel.setGeometry(QRect(50, 200, 200, 50))



window.show()

app.exec()