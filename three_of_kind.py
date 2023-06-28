p_cards = {
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

def check_three_of_a_kind(cards):
    card_values = [card[:-1] for card in cards]
    value_counts = {}
    for value in card_values:
        value_counts[value] = value_counts.get(value, 0) + 1
    for count in value_counts.values():
        if count == 3:
            return True
    return False

def three_of_a_kind():
    player_control_dic = result_card_dic()
    winners = []
    for player, cards in player_control_dic.items():
        if check_three_of_a_kind(cards):
            winners.append(player)
    return winners

print(three_of_a_kind())
