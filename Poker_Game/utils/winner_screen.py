from PyQt5 import QtWidgets, QtGui
from utils.ui.winner_screen_ui import Ui_MainWindow
from winner_check import Game
import random


class WinnerScreen(QtWidgets.QMainWindow):
    
    
    def __init__(self):
        super(WinnerScreen, self).__init__()
        self.screen = Ui_MainWindow()
        self.screen.setupUi(self)
        self.game = Game()
        self.screen.statistics_btn.clicked.connect(self.open_statistics_screen)
        self.screen.two_winner_btn.clicked.connect(self.two_winner)
        self.screen.Royalflush_btn.clicked.connect(self.royal_flush)
        self.screen.flush_straight_btn.clicked.connect(self.flush_straight)
        self.screen.four_btn.clicked.connect(self.four_of_a_kind)
        self.screen.full_button.clicked.connect(self.full_house)
        self.screen.flush_btn.clicked.connect(self.flush)
        self.screen.straight_btn.clicked.connect(self.straight)
        self.screen.three_btn.clicked.connect(self.three_of_a_kind)
        self.screen.two_btn.clicked.connect(self.two_pair)
        self.screen.one_btn.clicked.connect(self.one_pair)
        self.screen.higher_btn.clicked.connect(self.higher_card)
        
        
    def two_winner(self):
        self.count = 0
        while True:
            self.game.startGame()
            self.count += 1
            if len(self.game.winner_list) > 2:
                self.show_winner()
                
                break
            self.game.restartGame()
        self.game.restartGame()

    def open_statistics_screen(self):
        from utils.statistics_screen import StatisticsScreen
        self.hide()
        self.statistics_screen = StatisticsScreen()
        self.statistics_screen.show()

    def winner_option(self):
        while True:
            self.count += 1
            self.game.startGame()

            
            if self.option in self.game.winner_list:
                if len(self.game.winner_list) < 3:
                    self.show_winner()
                    #  DATABASE ICIN GEREKLI LISTELER
                    print(self.game.statistic_winner_hands)
                    print("\n\n\n")
                    print(self.game.statistic_all_hands)
                    
                    break
            self.game.restartGame()

        self.game.restartGame()

    def royal_flush(self):
        self.count = 0
        self.option = 'Royalflush'
        self.winner_option()

    def flush_straight(self):
        self.count = 0
        self.option = 'straight flush'
        self.winner_option()

    def four_of_a_kind(self):
        self.count = 0
        self.option = 'Four of a kind'
        self.winner_option()

    def full_house(self):
        self.count = 0
        self.option = 'Full house'
        self.winner_option()

    def flush(self):
        self.count = 0
        self.option = 'Flush'
        self.winner_option()

    def straight(self):
        self.count = 0
        self.option = 'Straight'
        self.winner_option()

    def three_of_a_kind(self):
        self.count = 0
        self.option = 'Three of a kind'
        self.winner_option()

    def two_pair(self):
        self.count = 0
        self.option = 'Two pair'
        self.winner_option()

    def one_pair(self):
        self.count = 0
        self.option = 'One pair'
        self.winner_option()

    def higher_card(self):
        self.count = 0
        self.option = 'Higher card'
        self.winner_option()

    def show_winner(self):
        self.screen.label_p1bet.setText('')
        self.screen.label_p2bet.setText('')
        self.screen.label_p3bet.setText('')
        self.screen.label_p4bet.setText('')
        self.screen.label_p5bet.setText('')
        self.screen.label_p6bet.setText('')

        self.screen.p1_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P1'][0]}.png"))
        self.screen.p1_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P1'][1]}.png"))
        self.screen.p2_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P2'][0]}.png"))
        self.screen.p2_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P2'][1]}.png"))
        self.screen.p3_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P3'][0]}.png"))
        self.screen.p3_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P3'][1]}.png"))
        self.screen.p4_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P4'][0]}.png"))
        self.screen.p4_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P4'][1]}.png"))
        self.screen.p5_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P5'][0]}.png"))
        self.screen.p5_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P5'][1]}.png"))
        self.screen.p6_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P6'][0]}.png"))
        self.screen.p6_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.players['P6'][1]}.png"))
        self.screen.desk_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.board_cards[0]}.png"))
        self.screen.desk_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.board_cards[1]}.png"))
        self.screen.desk_card3.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.board_cards[2]}.png"))
        self.screen.desk_card4.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.board_cards[3]}.png"))
        self.screen.desk_card5.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.board_cards[4]}.png"))
        if 'P1' in self.game.winner_list:
            self.screen.label_p1bet.setText('Winner')
        if 'P2' in self.game.winner_list:
            self.screen.label_p2bet.setText('Winner')
        if 'P3' in self.game.winner_list:
            self.screen.label_p3bet.setText('Winner')
        if 'P4' in self.game.winner_list:
            self.screen.label_p4bet.setText('Winner')
        if 'P5' in self.game.winner_list:
            self.screen.label_p5bet.setText('Winner')
        if 'P6' in self.game.winner_list:
            self.screen.label_p6bet.setText('Winner')

        self.screen.label_playerturn.setText(self.getWinnerList())

    def getWinnerList(self):
        res = ""
        for i in range(0, len(self.game.winner_list), 2):
            res +="Count: "+str(self.count) +"\n" +str(self.game.winner_list[i+1])
            break
        return res
    
    def getWinnerValues(self):
        res = ""
        for i in range(0, len(self.game.winner_list), 2):
            res +=self.game.winner_list[i]
            
        return res
