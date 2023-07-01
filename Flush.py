p_cards = {
    'P1': ['2H', '3C'],
    'P2': ['QD', 'KD'],
    'P3': ['QC', '5H'],
    'P4': ['3D', '3S'],
    'P5': ['6D', '8H'],
    'P6': ['5D', '10S']
}

c_cards = ['4C', 'AH', 'KH', 'QH', '9H']

def result_card_dic():
    player_control_dic = {}
    for player, cards in p_cards.items():
        a = []
        a.extend(cards)
        a.extend(c_cards)
        player_control_dic[player] = a
    return player_control_dic

suits_dic={}
player_control_dic=result_card_dic()

for player,cards in player_control_dic.items():
    new_list=[]
    for card in cards:
        new_list.append(card[-1])

    for suit in new_list:
        if new_list.count(suit)>4:
            # print(player,'full house var')
            rank_list=[]
            for card in cards:
                if card[-1]==suit:
                    rank_list.append(card[:-1])
            suits_dic[player]=rank_list


print(suits_dic)
