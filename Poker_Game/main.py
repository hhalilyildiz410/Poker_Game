import sys
from PyQt5 import QtWidgets
from utils.winner_screen import WinnerScreen
import sqlite3

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	winner_screen = WinnerScreen()
	winner_screen.show()
	sys.exit(app.exec_())




conn = sqlite3.connect("statistic.db")
curr=conn.cursor()
conn.commit()
table = curr.execute("create table if not exists urun (urunKodu int, urunAdi text, birimFiyati int)")
conn.commit()