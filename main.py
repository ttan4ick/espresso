import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.initUI()

    def initUI(self):
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Эспрессо")
        header = self.coffee_tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_compilation()

    def table_compilation(self):
        self.result = self.cur.execute(
            "SELECT id, sort_name, roasting_degree, type, taste, price, size FROM Coffee"
        ).fetchall()
        self.coffee_tableWidget.setRowCount(len(self.result))
        for i, film in enumerate(self.result):
            for j, information in enumerate(film):
                self.coffee_tableWidget.setItem(i, j, QTableWidgetItem(str(information)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())
