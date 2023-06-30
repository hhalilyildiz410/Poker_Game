p_cards = {
    'P1': ['JH', 'JH'],
    'P2': ['QD', 'AD'],
    'P3': ['JC', '5H'],
    'P4': ['3D', '3S'],
    'P5': ['6D', '8H'],
    'P6': ['5D', '10S']
}

c_cards=['4H', 'AH', 'KH', 'QH', '9H']

player_control_dic = {}
winner_list = []
values = {}


def result_card_dic():
    for i, j in p_cards.items():
        a = []
        a.extend(j)
        a.extend(c_cards)
        player_control_dic[i] = a
    return player_control_dic


def card_numeric():
    for player, cards in player_control_dic.items():
        numeric_values = []
        for card in cards:
            if card[0] == "A":
                numeric_values.append(14)
            elif card[0] == "K":
                numeric_values.append(13)
            elif card[0] == "Q":
                numeric_values.append(12)
            elif card[0] == "J":
                numeric_values.append(11)
            else:
                numeric_values.append(int(card[0]))

        numeric_values.sort(reverse=True)
        values[player] = sorted(numeric_values, reverse=True)
    return values


def four_of_a_kind():
    result_card_dic()
    card_numeric()

    four_of_a_kind_players = {}

    for player, cards in values.items():
        for i in range(len(cards) - 3):
            if cards[i] == cards[i + 1] == cards[i + 2] == cards[i + 3]:
                four_of_a_kind_players[player] = cards[i:i + 4]
                break

    if not four_of_a_kind_players:
        return "No four of a kind found."

    max_rank = max(cards[0] for cards in four_of_a_kind_players.values())

    winners = [player for player, cards in four_of_a_kind_players.items() if cards[0] == max_rank]

    if len(winners) > 1:
        return f"Winners: {', '.join(winners)}"
    else:
        return f"Winner: {winners[0]}"


sonuc = four_of_a_kind()
print(sonuc)
