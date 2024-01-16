import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from ui.loginForm import LoginForm
from db.db import DB


class MainWindow(qtw.QWidget):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        # init DB
        self.db = DB('test', 'test1234','pyqtDemos')

        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Lgin Form App Demos')
        self.setGeometry(400, 300, 300, 200)

        self.leAppHeader = qtw.QLabel('Welcome to my App')
        self.leAppHeader.setAlignment(
            qtc.Qt.AlignmentFlag.AlignHCenter |
            qtc.Qt.AlignmentFlag.AlignVCenter
        )
        self.leAppHeader.setFont(qtg.QFont('Arial', 16))

        self.btnLogin = qtw.QPushButton('Login')
        self.btnLogin.clicked.connect(self.onBtnLoginClick)

        self.btnRegistration = qtw.QPushButton('Registration')
        self.btnRegistration.clicked.connect(self.onBtnRegistrationClick)

        btnLayout = qtw.QHBoxLayout()
        btnLayout.addWidget(self.btnLogin)
        btnLayout.addWidget(self.btnRegistration)

        mainLayout = qtw.QVBoxLayout(self)
        mainLayout.setSpacing(60)

        mainLayout.addWidget(self.leAppHeader)
        mainLayout.addLayout(btnLayout)

        bottomSpacer = qtw.QSpacerItem(
            10, 10,
            qtw.QSizePolicy.Policy.Minimum, qtw.QSizePolicy.Policy.Expanding
        )
        mainLayout.addItem(bottomSpacer)


        self.show()

    def onBtnLoginClick(self):
        self.loginForm = LoginForm(parentWidget=self)
        self.loginForm.submit.connect(self.onLoginFormSubmit)
        self.loginForm.show()

    def onBtnRegistrationClick(self):
        qtw.QMessageBox.information(self,':)','This is your homework')

    def onLoginFormSubmit(self, userName, password):
        authenticated = self.db.authenticate(userName, password)
        self.loginForm.showLoginStatus(authenticated)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()

    sys.exit(app.exec())
