import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class LoginForm(qtw.QWidget):
    submit = qtc.pyqtSignal(str, str)

    def __init__(self , *args, **kwargs):
        super().__init__()
        self.setupUI()

        # connect signals
        self.btnLogin.clicked.connect(self.onLoginClick)
        self.btnCancel.clicked.connect(self.close) #type:ignore

    def setupUI(self):
        self.setWindowTitle('Login Form')
        self.setFixedSize(400,200)
        self.center_window()

        # create child widgets:
        self.leUserName = qtw.QLineEdit(self)
        self.lePassword = qtw.QLineEdit(self)
        self.lePassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        self.btnLogin = qtw.QPushButton('Login')
        self.btnCancel = qtw.QPushButton('Cancel')

        # create buttons layout:
        btnLayout = qtw.QHBoxLayout()
        btnLayout.addWidget(self.btnLogin,1)
        btnLayout.insertStretch(1,1)
        btnLayout.addWidget(self.btnCancel, 1)

        # create main Form layout
        mainLayout = qtw.QFormLayout(self)
        mainLayout.addRow('User Name', self.leUserName)
        mainLayout.addRow('Password', self.lePassword)
        mainLayout.addRow('', btnLayout)
        mainLayout.setVerticalSpacing(18)

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

    def onLoginClick(self):
        userName = self.leUserName.text()
        password = self.lePassword.text()

        self.submit.emit(userName, password)

    def showLoginStatus(self, authenticated):
        if authenticated:
            qtw.QMessageBox.information(self,'Login Successful','Login Successful')
        else:
            qtw.QMessageBox.critical(self,'Login failed','Login failed')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    loginForm = LoginForm()

    sys.exit(app.exec())
