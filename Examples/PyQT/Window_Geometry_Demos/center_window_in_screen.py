import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = qtw.QWidget()
    window.setWindowTitle('Center Window Demo')

    # Set window size and center it on the screen
    window_width = 400
    window_height = 400
    available_geometry = qtg.QGuiApplication.primaryScreen().availableGeometry()
    print(f'available_geometry={available_geometry}')

    window.setGeometry(
        (available_geometry.width() - window_width) // 2,
        (available_geometry.height() - window_height) // 2,
        window_width,
        window_height
    )

    window.show()
    sys.exit(app.exec())
