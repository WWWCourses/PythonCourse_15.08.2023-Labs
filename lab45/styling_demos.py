from ast import main
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.btn1 = qtw.QPushButton( '1')
        self.btn2 = qtw.QPushButton('2')

        self.btnLayout = qtw.QHBoxLayout()
        # self.btnLayout.setObjectName('btnLayout')
        self.btnLayout.addWidget(self.btn1)
        self.btnLayout.addWidget(self.btn2)

        self.btnWidget = qtw.QGroupBox()
        self.btnWidget.setLayout(self.btnLayout)

        self.lUserName = qtw.QLabel('User name: ')
        self.user_name = qtw.QLineEdit()
        self.btnLogin = qtw.QPushButton('Login')
        self.btnLogin.setObjectName('btnLogin')
        self.btnCanel = qtw.QPushButton('Cancel')

        self.userNameLayout = qtw.QHBoxLayout()
        self.userNameLayout.addWidget(self.lUserName)
        self.userNameLayout.addWidget(self.user_name)

        self.btnLoginLayout = qtw.QHBoxLayout()
        self.btnLoginLayout.addWidget(self.btnLogin)
        self.btnLoginLayout.addWidget(self.btnCanel)

        self.ml = qtw.QVBoxLayout()
        self.ml.addWidget(self.btnWidget)
        self.ml.addLayout(self.userNameLayout)
        self.ml.addLayout(self.btnLoginLayout)

        self.main_widget = qtw.QWidget()
        self.main_widget.setLayout(self.ml)

        self.setCentralWidget(self.main_widget)

        self.center_window()

        self.applyMainStyle()


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
    def applyMainStyle(self):
        with open('./main.css','r') as f:
            main_style=f.read()

        self.setStyleSheet(main_style)

    # def applyStyle(self):
    #     if self.btnLogin:
    #         self.btnLogin.setStyleSheet("""
    #             color: #f00;
    #             background-color: #000;
    #         """)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())