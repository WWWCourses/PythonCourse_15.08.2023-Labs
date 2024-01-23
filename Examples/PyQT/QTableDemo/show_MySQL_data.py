import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from db import DB


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		db = DB(user='test', password='test1234', db='pyqt_users_db')
		self.data = db.select_all_data()

		self.setWindowTitle('')

		lAppTitle = qtw.QLabel('Simplest Table Demo')
		lAppTitle.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
		self.table = self.uiCreateTable()

		ml = qtw.QVBoxLayout()
		ml.addWidget(lAppTitle)
		ml.addWidget(self.table)
		self.setLayout(ml)

		self.createTableAction()
		self.applyStyle()

	def uiCreateTable(self):
		rows = len(self.data)
		cols = len(self.data[0])

		# init table
		table = qtw.QTableWidget();
		table.setRowCount(rows);
		table.setColumnCount(cols);
		table.setHorizontalHeaderLabels(['id', 'username', 'password']);
		table.setMinimumHeight(cols*100);
		table.setMinimumWidth(rows*100);

		# set table values
		for row in range(rows):
			for col in range(cols):
				item = qtw.QTableWidgetItem(self.data[row][col])
				table.setItem(row, col, item)

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
