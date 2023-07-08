from PyQt5 import QtWidgets
from utils.ui.statistics_screen_ui import Ui_MainWindow



class StatisticsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(StatisticsScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.winner_btn.clicked.connect(self.open_winner_screen)
        self.ui.cards_submit_btn.clicked.connect(self.submit)
        self.ui.best_hands_btn.clicked.connect(self.best_hands)
        self.ui.Worst_Hands.clicked.connect(self.Worst_Hands)

    def open_winner_screen(self):
        from utils.winner_screen import WinnerScreen
        self.hide()
        self.winner_screen = WinnerScreen()
        self.winner_screen.show()

    def submit(self):
        self.ui.Summary_Table.setItem(0,1,QtWidgets.QTableWidgetItem('Poker'))
        # self.screen.label_p1bet.setText('Winner')
    
    def best_hands(self):
        pass
    
    def Worst_Hands(self):
        pass
    
    def sql_lite(self):
        import sqlite3
        conn = sqlite3.connect("urunler.db")
        curr=conn.cursor()
        conn.commit()
        table = curr.execute("create table if not exists urun (urunKodu int, urunAdi text, birimFiyati int)")
        conn.commit()