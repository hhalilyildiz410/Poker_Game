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


def check_flush(cards):
    suits = set(card[-1] for card in cards)
    if len(suits) == 1:  # All cards have the same suit
        return True
    return False

def flush():
    player_control_dic = result_card_dic()
    only_numeric={}
    for player,cards in player_control_dic.items():
        list=[]
        for card in cards:
            if card[:-1]=="A":
                list.append(14)

            elif card[:-1]=="K":
                list.append(13)

            elif card[:-1]=="Q":
                list.append(12)

            elif card[:-1] =="J":
                list.append(11)
            else:
                list.append(int(card[:-1]))
        only_numeric[player]=sorted(list,reverse=True)

    winners = []
    for player, cards in player_control_dic.items():
        if check_flush(cards):
            winners.append(player)
            flush_cards = [card[:-1] for card in cards if card[-1] == cards[0][-1]]
            print(f"Flush for {player}: {flush_cards}")
    return winners

print(flush())
