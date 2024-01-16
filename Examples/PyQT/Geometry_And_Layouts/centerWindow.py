import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Demo: Center Window ')

        self.setFixedSize(300, 200)

        self.center_window()
        self.show()

    def center_window(self):
        width = self.width()
        height = self.height()
        screen = qtg.QGuiApplication.primaryScreen()

        if screen:
            screen_geometry = screen.availableGeometry()

            self.setGeometry(
                (screen_geometry.width() - width) // 2,
                (screen_geometry.height() - height) // 2,
                width,
                height
            )


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()

    sys.exit(app.exec())
