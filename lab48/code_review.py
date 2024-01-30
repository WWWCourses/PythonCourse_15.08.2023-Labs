import sys
import os
import time
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QSizePolicy,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        self.second_window = None

        button = QPushButton("Open Second Window")
        button.clicked.connect(self.open_second_window)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)
        self.applyStyle()

    def applyStyle(self):
        self.setStyleSheet('''
            QWidget {
                border:5px solid red;
                font-size: 25px;
            }
            QLineEdit {
                border:5px solid blue;
                height: 30px;
                width: 300px
            }
        ''')

    def open_second_window(self):
        if self.second_window is None:
            self.second_window = LoginWindow()
        self.second_window.show()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")

        #Window containner
        container = QWidget()
        self.setCentralWidget(container)

        #Vertical layout
        layout = QVBoxLayout()
        container.setLayout(layout)

        #Username label and line edit
        self.username_label = QLabel("Username:")
        self.username_edit = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)

        #Password label and line edit
        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)

        #Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if username == "user" and password == "password":
            QMessageBox.information(self, "Success", "Login successful")
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

    print('################################################')





    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
        sys.exit(app.exec())
