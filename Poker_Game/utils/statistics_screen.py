import sqlite3

from PyQt5 import QtWidgets
from utils.ui.statistics_screen_ui import Ui_MainWindow


class StatisticsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(StatisticsScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.winner_btn.clicked.connect(self.open_winner_screen)
        self.ui.cards_submit_btn.clicked.connect(self.search)
        self.ui.best_hands_btn.clicked.connect(self.best)
        self.ui.Worst_Hands.clicked.connect(self.worst)
    def open_winner_screen(self):
        from utils.winner_screen import WinnerScreen
        self.hide()
        self.winner_screen = WinnerScreen()
        self.winner_screen.show()
    def search(self):
        self.baglanti=sqlite3.connect('statistik.db')
        self.cursor=self.baglanti.cursor()
        word=self.ui.cards_input.text()
        wordt=word[3:]+" "+ word[:2]
        print(wordt)
        self.cursor.execute('Select * From PokerStatistics')
        data=self.cursor.fetchall()
        print(data)
        new_data=[]
        for i in data:
           for j in i:
                if word in str(j) or wordt in str(j):
                    new_data.append(i)
                    break
        print(new_data)
        for row ,form in enumerate(new_data):
            for column,item in enumerate(form):
                self.ui.Summary_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(item)))
                column+=1
            row_position=self.ui.Summary_Table.rowCount()
            self.ui.Summary_Table.insertRow(row_position)
        
    def best(self):
        self.baglanti=sqlite3.connect('statistik.db')
        self.cursor=self.baglanti.cursor()
        self.cursor.execute('Select * From PokerStatistics order by winner_rate Desc Limit 11')
        data=self.cursor.fetchall()
        # print(data)
        for row ,form in enumerate(data):
            for column,item in enumerate(form):
                self.ui.Summary_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(item)))
                column+=1
            row_position=self.ui.Summary_Table.rowCount()
            self.ui.Summary_Table.insertRow(row_position)
    def worst(self):
        self.baglanti=sqlite3.connect('statistik.db')
        self.cursor=self.baglanti.cursor()
        self.cursor.execute('Select * From PokerStatistics order by winner_rate Asc Limit 11')
        data=self.cursor.fetchall()
        # print(data)
        for row ,form in enumerate(data):
            for column,item in enumerate(form):
                self.ui.Summary_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(item)))
                column+=1
            row_position=self.ui.Summary_Table.rowCount()
            self.ui.Summary_Table.insertRow(row_position)
