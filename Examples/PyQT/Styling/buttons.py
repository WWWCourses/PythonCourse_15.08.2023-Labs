import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from enum import Enum


class ButtonRole(Enum):
    DEFAULT = 'default'
    PRIMARY = 'primary'
    SUCCESS = 'success'
    DANGER = 'danger'
    WARNING = 'warning'
    INFO = 'info'


class StyledButton(qtw.QPushButton):
    COLOR_SCHEMES = {
        'primary': ('#007BFF', '#0056b3'),
        'success': ('#28a745', '#218838'),
        'danger': ('#DC3545', '#c82333'),
        'warning': ('#FFC107', '#e0a800'),
        'info': ('#17a2b8', '#138496'),
        'default': ('#6C757D', '#495057'),
    }
    def __init__(self, text, role=ButtonRole.DEFAULT, parent=None):
        super().__init__(text, parent)
        self.apply_stylesheet(role)
        self.setCursor(qtg.QCursor(qtc.Qt.CursorShape.PointingHandCursor))

    def apply_stylesheet(self, role=ButtonRole.DEFAULT):
        base_color, hover_color = self.COLOR_SCHEMES.get(
            role.value, self.COLOR_SCHEMES['default']
        )
        self.setStyleSheet(
            f'''
            QPushButton {{
                background-color: {base_color};
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            '''
        )


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = qtw.QWidget()
    w.setWindowTitle('Styled Buttons Demo')

    buttons = [
        StyledButton('Default'),
        StyledButton('Primary', role=ButtonRole.PRIMARY),
        StyledButton('Success', role=ButtonRole.SUCCESS),
        StyledButton('Danger', role=ButtonRole.DANGER),
        StyledButton('Warning', role=ButtonRole.WARNING),
        StyledButton('Info', role=ButtonRole.INFO),
    ]

    mainLayout = qtw.QGridLayout(w)
    columns = 2
    for idx, button in enumerate(buttons):
        row, col = divmod(idx, columns)
        mainLayout.addWidget(button, row, col)
    mainLayout.setSpacing(30)

    w.setGeometry(600,400, 300, 200)
    w.show()
    sys.exit(app.exec())
