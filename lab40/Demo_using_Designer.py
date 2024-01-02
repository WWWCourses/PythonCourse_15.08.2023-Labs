import sys

from PyQt6.QtWidgets import QApplication, QMainWindow


# from Ui_Test import Ui_Form
from Ui_QMainWindowDemo import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setupUi(self)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = Window()
  win.show()
  sys.exit(app.exec())