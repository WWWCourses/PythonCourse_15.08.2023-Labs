import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        btnClick = qtw.QPushButton('click')

        ml = qtw.QVBoxLayout(self)
        ml.addWidget(btnClick)

        self.apply_style()
        self.setGeometry(500, 400, 200, 150)

    def apply_style(self):
        style = """
            QPushButton{
                background-color: red
            }
        """
        self.setStyleSheet(style)
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())