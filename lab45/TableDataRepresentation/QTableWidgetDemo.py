import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(400, 300, 300, 300)
        self.applyStyle()
        self.setupTable()

    def applyStyle(self):
        style = """
            QTableWidget{
                border: 5px solid #f00;
            }
        """
        self.setStyleSheet(style)

    def setupTable(self):
        table =  qtw.QTableWidget(self)
        rows = len(data)
        cols = len(data[0])


        ### View
        table.setRowCount( rows )
        table.setColumnCount( cols )
        # TODO-DONE: headers MUST be set after setColumnCount(), otherwise it don't knowhow may columns are
        table.setHorizontalHeaderLabels(['A', 'B', 'C'])

        # table.resizeColumnsToContents()
        table.setMinimumWidth( cols*100 )
        # TODO-DONE: fix minHeight of rows
        table.verticalHeader().setMinimumSectionSize(50)


        ### Model
        # set data
        for row_idx, row in enumerate(data):
            for col_idx, el in enumerate(row):
                item = qtw.QTableWidgetItem( str(el) )
                table.setItem(row_idx,col_idx,item)


        # connect itemChanged signal:
        table.itemChanged.connect( self.onItemChage )

        self.table = table

    def onItemChage(self):
        row_idx = self.table.currentRow()
        col_idx = self.table.currentColumn()
        item = self.table.currentItem()
        if item:
            value = item.text()
            data[row_idx][col_idx] = int(value)

        print(data)



if __name__ == '__main__':
    # get data:
    data = [
        [1,2,3],
        [4,5,6]
    ]

    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())