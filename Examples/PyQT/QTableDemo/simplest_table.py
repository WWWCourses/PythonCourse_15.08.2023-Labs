import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		lAppTitle = qtw.QLabel('Simplest Table Demo')
		self.table =  self.uiCreateTable()
		ml = qtw.QVBoxLayout()
		ml.addWidget(lAppTitle)
		ml.addWidget(self.table)
		self.setLayout(ml)

		self.createTableAction()
		self.applyStyle()


	def uiCreateTable(self):
		rows = 4
		cols = 3

		# init table
		table = qtw.QTableWidget();
		table.setRowCount(rows);
		table.setColumnCount(cols);
		table.setHorizontalHeaderLabels(['Column1', 'Column2', 'Column3']);
		table.setMinimumHeight(cols*100);
		table.setMinimumWidth(rows*100);

		# set table values
		for row in range(rows):
			for col in range(cols):
				table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

		# resize cells to content:
		table.resizeColumnsToContents();
		table.resizeRowsToContents();

		return table

	def createTableAction(self):
		#  create our custom QActions
		self.table.add_above_action = qtg.QAction("Add row above", self.table)
		self.table.add_above_action.triggered.connect(lambda: self.table.insertRow(self.table.currentRow()))

	# DO NOT CALL IT - just rewrite
	def contextMenuEvent(self, event):
		# TODO: apply context menu only on table, not whole main widget
		context_menu = qtw.QMenu(self.table)
		context_menu.addAction(self.table.add_above_action)

		#HW: implement add row below custom action
		context_menu.addAction("Add row bellow")

		# By passing the event's position as argument we ensure that the context menu appears at the expected position.
		context_menu.exec(event.globalPos())

	def applyStyle(self):
		with open('./main.css') as f:
			content = f.read()

		self.setStyleSheet(content)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	window.show()

	sys.exit(app.exec())
