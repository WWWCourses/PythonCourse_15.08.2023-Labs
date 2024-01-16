import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

class Calc(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 400, 600)

        # Create the main layout
        main_layout = qtw.QVBoxLayout()

        # Create the display
        self.display = qtw.QLineEdit()
        self.display.setReadOnly(True)
        main_layout.addWidget(self.display)

        # Create the button grid layout
        buttons_layout = qtw.QGridLayout()
        buttons_layout.setSizeConstraint(qtw.QLayout.SizeConstraint.SetFixedSize)

        # create 1st row - span widgets horisontally by 2
        first_row_button_positions = [
            ('Backspace', 0, 0, 1, 2), ('Clear', 0, 2, 1, 3)
        ]
        for (text, row, col, row_span, col_span) in first_row_button_positions:
            button = qtw.QPushButton(text)
            # button.setSizePolicy(qtw.QSizePolicy.Policy.Fixed, qtw.QSizePolicy.Policy.Fixed)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            buttons_layout.addWidget(button, row, col, row_span, col_span)

        # Button positions
        rest_button_positions = [
            ('7', 1,0),('8', 1,1),('9',  1,2),('/', 1,3),('sqrt', 1,4),
            ('4', 2,0),('5', 2,1),('6',  2,2),('*', 2,3),('**2',  2,4),
            ('1', 3,0),('2', 3,1),('3',  3,2),('-', 3,3),('1/x',  3,4),
            ('0', 4,0),('.', 4,1),('+-', 4,2),('+', 4,3),('=',    4,4)
        ]

        for (text, row, col) in rest_button_positions:
            button = qtw.QPushButton(text)
            # button.setSizePolicy(qtw.QSizePolicy.Policy.Fixed, qtw.QSizePolicy.Policy.Fixed)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            buttons_layout.addWidget(button, row, col)


        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif text == 'Clear':
            self.display.clear()
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec())
