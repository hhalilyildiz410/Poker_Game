import sys
from PyQt5 import QtWidgets
from utils.winner_screen import WinnerScreen
import sqlite3

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	winner_screen = WinnerScreen()
	winner_screen.show()
	sys.exit(app.exec_())
