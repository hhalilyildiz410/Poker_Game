import random


class Game:
    symbol = ["C", "H", "S", "D"]

    def __init__(self,):
        self.deck_create()
        self.set_board_cards()
        self.players = {}
        self.winner_list = []
        self.player_control_dic = {}
        self.player_hand()
        self.result_card_dic()

    def restartGame(self):
        self.winner_list = []
        self.deck_create()
        self.set_board_cards()
        self.player_hand()
        self.result_card_dic()

    def startGame(self):
        self.check = False
        self.royalflush()
        if self.check == False:
            self.straight_flush()
        if self.check == False:
            self.four_of_a_kind()
        if self.check == False:
            self.full_house()
        if self.check == False:
            self.flush()
        if self.check == False:
            self.straight()
        if self.check == False:
            self.three_of_a_kind()
        if self.check == False:
            self.two_pair()
        if self.check == False:
            self.one_pair()
        if self.check == False:
            self.high_card()
        # print(self.winner_list)

    def deck_create(self):
        self.deck = []
        for i in Game.symbol:
            for j in range(2, 15):
                if j == 11:
                    j = "J"
                elif j == 12:
                    j = "Q"
                elif j == 13:
                    j = "K"
                elif j == 14:
                    j = "A"
                self.deck.append(str(j) + str(i))

    def player_hand(self):
        for i in range(1, 7):
            random_2 = random.sample(self.deck, k=2)
            self.deck.remove(random_2[0])
            self.deck.remove(random_2[1])
            self.players[f"P{i}"] = list(random_2)

    def set_board_cards(self):
        self.board_cards = []
        self.board_cards = random.sample(self.deck, 5)
        for i in range(5):
            self.deck.remove(self.board_cards[i])

    def result_card_dic(self):
        for i, j in self.players.items():
            a = [*j, *self.board_cards]
            self.player_control_dic[i] = a

    def get_only_numerics(self):
        only_numeric = {}
        for player, cards in self.player_control_dic.items():
            value = []
            for card in cards:
                if card[:-1] == "A":
                    value.append(14)
                elif card[:-1] == "K":
                    value.append(13)
                elif card[:-1] == "Q":
                    value.append(12)
                elif card[:-1] == "J":
                    value.append(11)
                else:
                    value.append(int(card[:-1]))
            only_numeric[player] = sorted(value, reverse=True)
        return only_numeric

    def royalflush(self):
        for i, j in self.player_control_dic.items():
            royalclubs = ["AC", "KC", "QC", "JC", "10C"]
            a = []
            a.extend(j)
            for element in royalclubs:
                if element in a:
                    a.remove(element)
            x = len(a)
            if x == 2:
                self.winner_list.append(i)
                self.winner_list.append('Royalflush')
                self.check = True

        for i, j in self.player_control_dic.items():
            royaldiamonds = ["AD", "KD", "QD", "JD", "10D"]
            a = []
            a.extend(j)
            for element in royaldiamonds:
                if element in a:
                    a.remove(element)
            x = len(a)
            if x == 2:
                self.winner_list.append(i)
                self.winner_list.append('Royalflush')
                self.check = True

        for i, j in self.player_control_dic.items():
            royalhearts = ["AH", "KH", "QH", "JH", "10H"]
            a = []
            a.extend(j)
            for element in royalhearts:
                if element in a:
                    a.remove(element)
            x = len(a)
            if x == 2:
                self.winner_list.append(i)
                self.winner_list.append('Royalflush')
                self.check = True

        for i, j in self.player_control_dic.items():
            royalspades = ["AS", "KS", "QS", "JS", "10S"]
            a = []
            a.extend(j)
            for element in royalspades:
                if element in a:
                    a.remove(element)
            x = len(a)
            if x == 2:
                self.winner_list.append(i)
                self.winner_list.append('Royalflush')
                self.check = True

    def straight_flush(self):
        player_wins = {}
        for player, cards in self.player_control_dic.items():
            all_cards = cards
            suits = set(card[-1] for card in all_cards)
            if len(suits) == 1:  # Tüm kartlar aynı renkte
                card_values = [card[:-1] for card in all_cards]
                card_ranks = {
                    'A': 14,
                    'K': 13,
                    'Q': 12,
                    'J': 11,
                    '10': 10,
                    '9': 9,
                    '8': 8,
                    '7': 7,
                    '6': 6,
                    '5': 5,
                    '4': 4,
                    '3': 3,
                    '2': 2
                }
                sorted_values = sorted(
                    card_ranks[card_value] for card_value in card_values)
                for i in range(len(sorted_values) - 4):
                    if sorted_values[i] == sorted_values[i + 1] - 1 == sorted_values[i + 2] - 2 == sorted_values[i + 3] - 3 == sorted_values[i + 4] - 4:
                        if player not in player_wins:
                            player_wins[player] = 0
                        player_wins[player] += 1
                        break
            else:
                player_wins[player] = 0
        try:
            max_rank = max(player_wins.values())
            for player, rank in player_wins.items():
                if rank == max_rank and rank != 0:
                    self.winner_list.append(player)
                    self.winner_list.append("straight flush")
                    self.check = True
        except:
            pass

    def four_of_a_kind(self):
        four_of_a_kind_players = {}

        for player, cards in self.get_only_numerics().items():
            for i in range(len(cards) - 3):
                if cards[i] == cards[i + 1] == cards[i + 2] == cards[i + 3]:
                    four_of_a_kind_players[player] = cards[i:i + 4]
                    break

        if not four_of_a_kind_players:
            return "No four of a kind found."

        try:
            max_rank = max(cards[0]
                           for cards in four_of_a_kind_players.values())
        except:
            pass

        for player, cards in four_of_a_kind_players.items():
            if cards[0] == max_rank:
                self.winner_list.append(player)
                self.winner_list.append("Four of a kind")
                self.check = True

    def full_house(self):
        pairs = {}

        for player, cards in self.get_only_numerics().items():
            triple = []
            double = []
            for card in cards:
                count = cards.count(card)
                if count == 3:
                    if card not in triple:
                        triple.append(card)
                if count == 2:
                    if card not in double:
                        double.append(card)

            if len(triple) == 1 and len(double) != 0:
                triple.append(double[0])
                pairs[player] = triple
            elif len(triple) == 2:
                pairs[player] = triple
        try:
            max_values = max(pairs.values())
        except:
            pass

        for player, cards in pairs.items():
            if cards[:2] == max_values[:2]:
                self.winner_list.append(player)
                self.winner_list.append('Full house')
                self.check = True

    def flush(self):
        suits_dic = {}
        for player, cards in self.player_control_dic.items():
            suit_list = []
            for card in cards:
                suit_list.append(card[-1])

            for suit in suit_list:
                if suit_list.count(suit) > 4:

                    rank_list = []
                    for card in cards:
                        if card[-1] == suit:
                            rank_list.append(card[:-1])
                    suits_dic[player] = rank_list
        try:
            maxVal = max(suits_dic.values())
            for player, cards in suits_dic.items():
                if cards == maxVal:
                    self.winner_list.append(player)
                    self.winner_list.append('Flush')
                    self.check = True
        except:
            pass

    def straight(self):

        duzenli_ardisik_dict = {}
        only_new_numeric = {}
        for player, cards in self.get_only_numerics().items():

            uniq_cards = []
            for i in range(len(cards)):

                if cards[i] not in uniq_cards:
                    uniq_cards.append(cards[i])

            only_new_numeric[player] = uniq_cards

        for player, cards in only_new_numeric.items():
            for i in range(len(cards) - 4):
                if cards[i] == cards[i+4]+4:
                    duzenli_ardisik_dict[player] = cards[i:i+5]
                    break

        winners = {}
        for player, cards in duzenli_ardisik_dict.items():
            winners[player] = self.player_control_dic[player]

        last_winner = {}

        for player, cards in winners.items():
            same_suit_count = 0
            for suit in ['H', 'S', 'C', 'D']:
                suit_cards = [card for card in cards if card.endswith(suit)]
                if len(suit_cards) > 4:
                    same_suit_count += 1
            if same_suit_count == 0:
                last_winner[player] = cards

        try:
            for key, value in last_winner.items():
                if value == max(last_winner.values()):
                    self.winner_list.append(player)
                    self.winner_list.append('Straight')
                    self.check = True
        except:
            pass

    # def check_three_of_a_kind(cards):
    #     card_values = [card[:-1] for card in cards]
    #     value_counts = {}
    #     for value in card_values:
    #         value_counts[value] = value_counts.get(value, 0) + 1
    #     for count in value_counts.values():
    #         if count == 3:
    #             return True
    #     return False
    def three_of_a_kind(self):
        highest_rank = 0

        only_numeric = self.get_only_numerics()

        for player, cards in only_numeric.items():
            value_counts = {}
            for value in cards:
                value_counts[value] = value_counts.get(value, 0) + 1
                for value, count in value_counts.items():
                    if count == 3:
                        rank = value
                        if rank > highest_rank:
                            highest_rank = rank
                            self.winner_list = [player, 'Three of a kind']
                            self.check = True
                        elif rank == highest_rank:
                            self.winner_list = [player, 'Three of a kind']
                            self.check = True

    # def three_of_a_kind(self):
    #     for player, cards in self.player_control_dic.items():
    #         card_values = [card[:-1] for card in cards]
    #         value_counts = {}
    #         for value in card_values:
    #             value_counts[value] = value_counts.get(value, 0) + 1
    #         for count in value_counts.values():
    #             if count == 3:
    #                 self.winner_list.append(player)
    #                 self.winner_list.append("Three of a kind")
    #                 self.check = True

    #     highest_rank = 0
    #     for player, cards in self.player_control_dic.items():
    #         if Game.check_three_of_a_kind(cards):
    #             card_values = [card[:-1] for card in cards]
    #             value_counts = {}
    #             for value in card_values:
    #                 value_counts[value] = value_counts.get(value, 0) + 1
    #             for value, count in value_counts.items():
    #                 if count == 3:
    #                     self.rank = Game.get_card_rank(value)
    #                     if self.rank > highest_rank:
    #                         highest_rank = self.rank
    #                         self.winner_list.append(player)
    #                         self.winner_list.append("three of a kind")
    #                         self.check=True
    #                     elif self.rank == highest_rank:
    #                         self.winner_list.append(player)
    #                         self.winner_list.append("three of a kind")
    #                         self.check=True

    # def get_card_rank(self,value):
    #     ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    #     return ranks.get(value, 0)

    def two_pair(self):
        pairs_dic = {}

        for player, cards in self.get_only_numerics().items():
            double = []
            een = []
            pair = []
            for card in cards:
                count = cards.count(card)
                if count == 2:
                    if card not in double:
                        double.append(card)
                if count == 1:
                    if card not in een:
                        een.append(card)
            if len(double) >= 2:
                pair.extend(double[:2])
                pair.append(een[0])
                pairs_dic[player] = pair
        try:
            for player, cards in pairs_dic.items():

                if cards == max(pairs_dic.values()):
                    self.winner_list.append(player)
                    self.winner_list.append('Two pair')
                    self.check = True

        except:
            pass

    def one_pair(self):
        one_pairs_dict = {}

        for player, cards in self.get_only_numerics().items():
            for card in cards:
                if len(set(cards)) == 6:
                    if cards.count(card) == 2 and player not in one_pairs_dict:
                        one_pairs_dict[player] = cards
        try:
            max_values = max(one_pairs_dict.values())
            for player, cards in one_pairs_dict.items():
                if sorted(cards[:6], reverse=True) == max_values[:6]:
                    self.winner_list.append(player)
                    self.winner_list.append('One pair')
                    self.check = True

        except:
            pass

    def high_card(self):

        try:
            max_values = max(self.get_only_numerics().values())
            for player, cards in self.get_only_numerics().items():
                if cards[:5] == max_values[:5]:
                    self.winner_list.append(player)
                    self.winner_list.append('Higher card')
                    self.check = True

        except:
            pass


# game = Game()
# print(game.players)
# print(game.player_control_dic)
# print(game.board_cards)
# game.startGame()
# print(game.winner_list)
