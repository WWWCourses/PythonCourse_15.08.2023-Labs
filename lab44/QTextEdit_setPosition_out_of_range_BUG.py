import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        editor = qtw.QTextEdit( )
        # editor.setPlainText("a")
        self.setCentralWidget(editor)


        ### Fix Bug: Attempt 1: setCursorPosition to 0:
        # editor.textCursor().setPosition(0)
        # print(f'cursor position: {editor.textCursor().position()}')


        ### Fix Bug: Attempt 2: move coursor to start of line
        # cursor = editor.textCursor()
        # cursor.movePosition(qtg.QTextCursor.MoveOperation.StartOfLine)
        # editor.setTextCursor(cursor)
        # print(f'cursor position: {editor.textCursor().position()}')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())