

p_cards = {
    'P1': ['JH', '10H'],
    'P2': ['QD', 'KD'],
    'P3': ['QC', '5H'],
    'P4': ['3D', '3S'],
    'P5': ['6D', '8H'],
    'P6': ['5D', '10S']
}


c_cards = ['4H', 'AH', 'KH', 'QH', '9H']

def find_flush(cards):
    flushes = []
    suits = set(card[-1] for card in cards)
    for suit in suits:
        suit_cards = [card for card in cards if card[-1] == suit]
        if len(suit_cards) >= 5:
            flushes.extend(suit_cards, 5)
    return flushes

winners = []
for player, cards in p_cards.items():
    flushes = find_flush(cards)
    if flushes:
        winners.append(player)
        for flush in flushes:
            print(f"Flush for {player}: {flush}")
            
print("Winners:", winners)
