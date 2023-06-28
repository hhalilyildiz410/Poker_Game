‌p_cards = {
    'P1': ['JH', '10H'],
    'P2': ['QD', 'KD'],
    'P3': ['QC', '5H'],
    'P4': ['3D', '3S'],
    'P5': ['6D', '8H'],
    'P6': ['5D', '10S']
}

c_cards = ['4H', 'AH', 'KH', 'QH', '9H']

def result_card_dic():
    player_control_dic = {}
    for player, cards in p_cards.items():
        a = []
        a.extend(cards)
        a.extend(c_cards)
        player_control_dic[player] = a
    return player_control_dic

def check_straight_flush(cards):
    suits = set(card[-1] for card in cards)
    if len(suits) == 1:  # All cards have the same suit
        card_values = [card[:-1] for card in cards]
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
        sorted_values = sorted(card_ranks[card_value] for card_value in card_values)
        for i in range(len(sorted_values) - 4):
            if sorted_values[i] == sorted_values[i + 1] - 1 == sorted_values[i + 2] - 2 == sorted_values[i + 3] - 3 == sorted_values[i + 4] - 4:
                return True
    return False

    def straight_flush():
    player_control_dic = result_card_dic()
    winners = []
    for player, cards in player_control_dic.items():
        if check_straight_flush(cards):
            winners.append(player)
    return winners

    print(straight_flush())
