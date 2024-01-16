import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
import re

class MainWindow(qtw.QMainWindow):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        self.create_actions()
        self.create_menu_bar()
        self.create_toolbar()
        self.create_doc_widget()
        self.create_status_bar()

        self.setWindowTitle('My Simple Text Editor')
        self.setWindowIcon(qtg.QIcon('./icons/text_editor_icon.png'))
        self.resize(800, 600)
        self.set_style()
        self.show()

    def create_actions(self):
        self.openAction = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogOpenButton), #type:ignore
            "&Open...",
            self
        )
        self.openAction.triggered.connect(self.open_new_file)

        self.saveAction = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogSaveButton), #type:ignore
            "&Save",
            self
        )
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save your changes")
        self.saveAction.triggered.connect(self.save_file)

        self.exitAction = qtg.QAction("&Exit", self)

        self.about_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogHelpButton), #type:ignore
            '&About',
            self  # important to pass the parent!
        )
        # add signal
        self.about_action.triggered.connect(lambda : qtw.QMessageBox.information(
            self,
            'My Simple Text Editor',
            '@2022, Created by ME, no rights reserved!')
        )


    def create_menu_bar(self):
        # add menu items
        menubar:qtw.QMenuBar = self.menuBar()   # type:ignore
        file_menu:qtw.QMenu = menubar.addMenu('&File') # type:ignore
        file_menu.addAction(self.openAction)
        file_menu.addAction(self.saveAction)

        edit_menu:qtw.QMenu = menubar.addMenu('&Edit') # type:ignore

        help_menu:qtw.QMenu = menubar.addMenu('&Help') # type:ignore
        help_menu.addAction(self.about_action)

    def create_toolbar(self):
        toolbar:qtw.QToolBar = self.addToolBar('File') # type:ignore
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)
        toolbar.addAction(self.about_action)

        toolbar.setMovable(True)
        toolbar.setFloatable(False)
        toolbar.setAllowedAreas(
            qtc.Qt.ToolBarArea.TopToolBarArea |
            qtc.Qt.ToolBarArea.BottomToolBarArea
        )

    def create_doc_widget(self):
        dock = qtw.QDockWidget("File actions")
        self.addDockWidget(qtc.Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        # set dock widget to move and float (but not closeable)
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetFeature.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )

        replace_widget = qtw.QWidget()

        self.search_text_input = qtw.QLineEdit()
        self.search_text_input.setPlaceholderText('search')
        self.replace_text_input = qtw.QLineEdit()
        self.replace_text_input.setPlaceholderText('replace')

        search_and_replace_btn = qtw.QPushButton("Search and Replace")
        search_and_replace_btn.clicked.connect(self.search_and_replace)

        replace_widget.setLayout(qtw.QVBoxLayout())
        replace_widget_layout:qtw.QVBoxLayout = replace_widget.layout() # type:ignore
        replace_widget_layout.addWidget(self.search_text_input)
        replace_widget_layout.addWidget(self.replace_text_input)
        replace_widget_layout.addWidget(search_and_replace_btn)
        replace_widget_layout.addStretch()

        dock.setWidget(replace_widget)

    def create_status_bar(self):
        # create status bar widget and atach it to main window:
        self.status_bar = qtw.QStatusBar()
        self.setStatusBar(self.status_bar)

        # show temporary message for 3 second:
        self.status_bar.showMessage('Welcome to My Text Editor',3000)

        charcount_label = qtw.QLabel("chars: 0")
        self.textedit.textChanged.connect(
            lambda: charcount_label.setText( "chars: " + str(len(self.textedit.toPlainText())) )
        )
        self.status_bar.addPermanentWidget(charcount_label)

    @qtc.pyqtSlot()
    def open_new_file(self):
        self.file_path, filter_type = qtw.QFileDialog.getOpenFileName(self, "Open new file","", "All files (*)")
        if self.file_path:
            with open(self.file_path, "r") as f:
                file_contents = f.read()
                self.setWindowTitle(self.file_path)
                self.textedit.setText(file_contents)

    @qtc.pyqtSlot()
    def save_file(self):
        self.file_path, _ = qtw.QFileDialog.getSaveFileName(self, "Save as","", "All files (*)")
        if self.file_path:
            with open(self.file_path, "w") as f:
                content = self.textedit.toPlainText()
                f.write(content)
                self.setWindowTitle(self.file_path)


    @qtc.pyqtSlot(bool)
    def search_and_replace(self):
        print('search_and_replace')
        search_text = self.search_text_input.text()
        replace_text = self.replace_text_input.text()

        text_to_search =  self.textedit.toPlainText()

        regex = re.compile(fr'{search_text}')
        replaced_text = regex.sub(replace_text,text_to_search)
        self.textedit.setPlainText(replaced_text)

    def set_style(self):
        main_style = """
            QTextEdit{
                background: #222;
                color: #CCC;
            }

            QTextEdit:focus{
                border: 2px solid #F99;
            }
        """
        self.setStyleSheet(main_style)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()

    sys.exit(app.exec())
