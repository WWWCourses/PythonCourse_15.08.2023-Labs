import sys


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

class RowHeightSlider(QSlider):
    def __init__(self, parent=None):
        #QSlider.__init__(self, parent)
        super(RowHeightSlider, self).__init__(parent)
        self.setOrientation(Qt.Horizontal)
        self.setMinimum(4)
        self.setMaximum(72)
        self.setSingleStep(1)
        self.setPageStep(2)
        self.setTickPosition(QSlider.TicksAbove)
        self.setTickInterval(1)

class Window(QWidget):
    def __init__(self, parent=None):
        #QWidget.__init__(self, parent)
        super(Window, self).__init__(parent)
        self.parentModel = QSqlQueryModel(self)
        self.refreshParent()
        self.parentProxyModel = QSortFilterProxyModel()
        self.parentProxyModel.setSourceModel(self.parentModel)
        self.parentView = QTableView()
        self.parentView.setModel(self.parentProxyModel)
        self.parentView.setSelectionMode(QTableView.SingleSelection)
        self.parentView.setSelectionBehavior(QTableView.SelectRows)
        self.parentView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.parentView.horizontalHeader().setStretchLastSection(True)
        self.parentView.verticalHeader().setVisible(False)
        self.parentView.setSortingEnabled(True)
        self.parentView.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        self.parentView.setAlternatingRowColors(True)
        self.parentView.setShowGrid(False)
        #self.parentView.verticalHeader().setDefaultSectionSize(24)
        self.parentView.setStyleSheet("QTableView::item:selected:!active { selection-background-color:#BABABA; }")
        for i, header in enumerate(self.parentHeaders):
            self.parentModel.setHeaderData(i, Qt.Horizontal, self.parentHeaders[self.parentView.horizontalHeader().visualIndex(i)])
        self.parentView.resizeColumnsToContents()

        self.childModel = QSqlQueryModel(self)
        self.refreshChild()
        self.childProxyModel = QSortFilterProxyModel()
        self.childProxyModel.setSourceModel(self.childModel)
        self.childView = QTableView()
        self.childView.setModel(self.childProxyModel)
        self.childView.setSelectionMode(QTableView.SingleSelection)
        self.childView.setSelectionBehavior(QTableView.SelectRows)
        self.childView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.childView.horizontalHeader().setStretchLastSection(True)
        self.childView.verticalHeader().setVisible(False)
        self.childView.setSortingEnabled(True)
        self.childView.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        self.childView.setAlternatingRowColors(True)
        self.childView.setShowGrid(False)
        #self.childView.verticalHeader().setDefaultSectionSize(24)
        self.childView.setStyleSheet("QTableView::item:selected:!active { selection-background-color:#BABABA; }")
        for i, header in enumerate(self.childHeaders):
            self.childModel.setHeaderData(i, Qt.Horizontal, self.childHeaders[self.childView.horizontalHeader().visualIndex(i)])
        self.childView.resizeColumnsToContents()

        self.parentSlider = RowHeightSlider()
        self.childSlider = RowHeightSlider()

        self.parentRowHeightLabel = QLabel('Row height: 32')
        self.childRowHeightLabel = QLabel('Row height: 32')

        parentLayout = QVBoxLayout()
        parentLayout.addWidget(self.parentSlider)
        parentLayout.addWidget(self.parentRowHeightLabel)
        parentLayout.addWidget(self.parentView)

        childLayout = QVBoxLayout()
        childLayout.addWidget(self.childSlider)
        childLayout.addWidget(self.childRowHeightLabel)
        childLayout.addWidget(self.childView)

        layout = QHBoxLayout()
        layout.addLayout(parentLayout)
        layout.addLayout(childLayout)
        self.setLayout(layout)

        self.parentView.selectionModel().currentRowChanged.connect(self.parentChanged)
        self.parentSlider.valueChanged.connect(self.changeParentRowHeight)
        self.childSlider.valueChanged.connect(self.changeChildRowHeight)

        self.parentView.setCurrentIndex(self.parentView.model().index(0, 0))
        self.parentView.setFocus()

        self.parentSlider.setValue(36)
        self.childSlider.setValue(36)

    def refreshParent(self):
        self.parentHeaders = ['Parent']
        queryString = "SELECT parent.parent_name FROM parent"
        query = QSqlQuery()
        query.exec(queryString)
        self.parentModel.setQuery(query)
        while self.parentModel.canFetchMore():
            self.parentModel.fetchMore()

    def refreshChild(self, parent_name=''):
        self.childHeaders = ['Child']
        queryString = ("SELECT child.child_name FROM child "
            "WHERE child.parent_name = '{parent_name}'").format(parent_name = parent_name)
        query = QSqlQuery()
        query.exec(queryString)
        self.childModel.setQuery(query)
        while self.childModel.canFetchMore():
            self.childModel.fetchMore()

    def parentChanged(self, index):
        if index.isValid():
            index = self.parentProxyModel.mapToSource(index)
            record = self.parentModel.record(index.row())
            self.refreshChild(record.value("parent.parent_name"))
            #self.childView.scrollToBottom() # if needed

    def changeParentRowHeight(self, rowHeight):
        parentVerticalHeader = self.parentView.verticalHeader()

        # (any)one of these two rows (or both) has to be uncommented
        parentVerticalHeader.setMinimumSectionSize(rowHeight)
        #parentVerticalHeader.setMaximumSectionSize(rowHeight)

        for section in range(parentVerticalHeader.count()):
            parentVerticalHeader.resizeSection(section, rowHeight)
        self.displayParentRowHeightLabel(rowHeight)

    def changeChildRowHeight(self, rowHeight):
        childVerticalHeader = self.childView.verticalHeader()

        # (any)one of these two rows (or both) has to be uncommented
        childVerticalHeader.setMinimumSectionSize(rowHeight)
        #childVerticalHeader.setMaximumSectionSize(rowHeight)

        for section in range(childVerticalHeader.count()):
            childVerticalHeader.resizeSection(section, rowHeight)
        self.displayChildRowHeightLabel(rowHeight)

    def displayParentRowHeightLabel(self, rowHeight):
        visibleRows = self.parentView.rowAt(self.parentView.height()) - self.parentView.rowAt(0)
        if self.parentView.rowAt(self.parentView.height()) == -1:
            visibleRowsString = str(self.parentView.model().rowCount()) + '+'
        else:
            visibleRowsString = str(visibleRows)
        self.parentRowHeightLabel.setText('Row height: ' + str(rowHeight) + ', Visible rows: ' + visibleRowsString)

    def displayChildRowHeightLabel(self, rowHeight):
        visibleRows = self.childView.rowAt(self.childView.height()) - self.childView.rowAt(0)
        if self.childView.rowAt(self.childView.height()) == -1:
            visibleRowsString = str(self.childView.model().rowCount()) + '+'
        else:
            visibleRowsString = str(visibleRows)
        self.childRowHeightLabel.setText('Row height: ' + str(rowHeight) + ', Visible rows: ' + visibleRowsString)

    def resizeEvent(self, event):
        # make it resize-friendly
        self.displayParentRowHeightLabel(self.parentSlider.value())
        self.displayChildRowHeightLabel(self.childSlider.value())

def createFakeData():
    parent_names = []
    #import random
    query = QSqlQuery()
    query.exec("CREATE TABLE parent(parent_name TEXT)")
    for i in range(1, 101):
        parent_num = str(i).zfill(3)
        parent_name = 'parent_name_' + parent_num
        parent_names.append((parent_name, parent_num))
        query.prepare("INSERT INTO parent (parent_name) VALUES(:parent_name)")
        query.bindValue(":parent_name", parent_name)
        query.exec()
    query.exec("CREATE TABLE child(parent_name TEXT, child_name TEXT)")
    counter = 1
    for parent_name, parent_num in parent_names:
        for i in range(1, 101):
            child_name = 'child_name_' + parent_num + '_' + str(counter).zfill(5)
            counter += 1
            query.prepare("INSERT INTO child (parent_name, child_name) VALUES(:parent_name, :child_name)")
            query.bindValue(":parent_name", parent_name)
            query.bindValue(":child_name", child_name)
            query.exec()

def createConnection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    #db.setDatabaseName("test04.db")
    db.setDatabaseName(":memory:")
    db.open()
    createFakeData()

app = QApplication(sys.argv)
createConnection()
window = Window()
window.resize(800, 600)
#window.show()
window.showMaximized()
app.exec()