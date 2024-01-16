import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class ReplaceWidget(qtw.QWidget):
    # TODO : not visualized ...
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        replace_widget = qtw.QWidget()

        self.search_text_input = qtw.QLineEdit()
        self.search_text_input.setPlaceholderText('search')
        self.replace_text_input = qtw.QLineEdit()
        self.replace_text_input.setPlaceholderText('replace')

        search_and_replace_btn = qtw.QPushButton("Search and Replace")
        search_and_replace_btn.clicked.connect(self.search_and_replace)

        replace_widget.setLayout(qtw.QVBoxLayout())
        replace_widget.layout().addWidget(self.search_text_input)
        replace_widget.layout().addWidget(self.replace_text_input)
        replace_widget.layout().addWidget(search_and_replace_btn)
        replace_widget.layout().addStretch()

    def search_and_replace(self):
        print('Search Button clicked')


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        self.createActions()
        self.createMenuBar()
        self.createToolBar()
        self.createDock()

    def createActions(self):
        self.open = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DirOpenIcon), # type:ignore
            'Open',
            self  # important to pass the parent!
        )
        self.open.triggered.connect(self.onOpen)

    def createDock(self):
        dock = qtw.QDockWidget("Replace")
        self.addDockWidget(qtc.Qt.DockWidgetArea.LeftDockWidgetArea, dock) # type:ignore

        # set dock widget to move and float (but not closeable)
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetFeature.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )

        self.replaceWidget = ReplaceWidget()
        dock.setWidget(self.replaceWidget)

    def createMenuBar(self):
        # get the menu bar
        menubar:qtw.QMenuBar = self.menuBar() #type:ignore

        # add menu items
        file_menu = menubar.addMenu('&File')
        edit_menu = menubar.addMenu('E&dit')
        help_menu = menubar.addMenu('Help')

        file_menu.addAction(self.open)

    def createToolBar(self):
        toolbar = self.addToolBar('File') #
        if toolbar:
            toolbar.setMovable(True)
            toolbar.setFloatable(True)

            # for Qt6:
            toolbar.setAllowedAreas(
                qtc.Qt.ToolBarArea.TopToolBarArea |
                qtc.Qt.ToolBarArea.BottomToolBarArea
            )

    def onOpen(self):
        print('Open')



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())