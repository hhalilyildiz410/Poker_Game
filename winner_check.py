import random

symbol=["C","H","S","D"]
deck=[]

for i in symbol:
    for j in range(2,15) :
        if j ==11:
            j="J"
        elif j ==12:
            j="Q"
        elif j == 13:
            j="K"
        elif j ==14:
            j="A"
        deck.append(str(j)+str(i))


deck_5=random.sample(deck,5)

for i in range(5):
    deck.remove(deck_5[i])

players={}
for i in range(1,7):
    random_2=random.sample(deck,k=2)
    deck.remove(random_2[0])
    deck.remove(random_2[1])
    players[f"P{i}"]=random_2

player_control_dic={}
def result_card_dic():
    for i,j in players.items():
            a=[]
            a.extend(j)
            a.extend(deck_5)
            player_control_dic[i]=a



def only_numerics():
    result_card_dic()

    only_numeric={}
    for player,cards in player_control_dic.items():
        value=[]
        for card in cards:
            if card[:-1]=="A":
                value.append(14)

            elif card[:-1]=="K":
                value.append(13)

            elif card[:-1]=="Q":
                value.append(12)

            elif card[:-1] =="J":
                value.append(11)
            else:
                value.append(int(card[:-1]))
        only_numeric[player]=sorted(value,reverse=True)
    return only_numeric
check=False

def royalflush():
    global check
    result_card_dic()
    winner_list=[]
    for i ,j in player_control_dic.items():
        royalclubs=["AC","KC","QC","JC","10C"]
        a=[]
        a.extend(j)
        for element in royalclubs:
            if element in a:
                a.remove(element)
        x=len(a)
        if x==2:
            winner_list.append(i)
            winner_list.append('RoyalFlush')
            print('Heart Royal Flush')
            check=True

    for i ,j in player_control_dic.items():
        royaldiamonds=["AD","KD","QD","JD","10D"]
        a=[]
        a.extend(j)
        for element in royaldiamonds:
            if element in a:
                a.remove(element)
        x=len(a)
        if x==2:
            winner_list.append(i)
            winner_list.append('Royalflush')
            print('var D')
            check=True

    for i ,j in player_control_dic.items():
        royalhearts=["AH","KH","QH","JH","10H"]
        a=[]
        a.extend(j)
        for element in royalhearts:
            if element in a:
                a.remove(element)
        x=len(a)
        if x==2:
            winner_list.append(i)
            winner_list.append('Royalflush')
            print('var H')
            check=True

    for i ,j in player_control_dic.items():
        royalspades=["AS","KS","QS","JS","10S"]
        a=[]
        a.extend(j)
        for element in royalspades:
            if element in a:
                a.remove(element)
        x=len(a)
        if x==2:
            winner_list.append(i)
            winner_list.append('Royalflush')
            print('var S')
            check=True

royalflush()


def straight_flush():
    global check
    player_wins = {}
    for player, cards in player_control_dic.items():
        all_cards = cards + deck_5
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
            sorted_values = sorted(card_ranks[card_value] for card_value in card_values)
            for i in range(len(sorted_values) - 4):
                if sorted_values[i] == sorted_values[i + 1] - 1 == sorted_values[i + 2] - 2 == sorted_values[i + 3] - 3 == sorted_values[i + 4] - 4:
                    straight_flush_exists = True
                    if player not in player_wins:
                        player_wins[player] = 0
                    player_wins[player] += 1
                    break
        else:
            player_wins[player] = 0
            check= False
    max_rank = max(player_wins.values())
    winners = [player for player, rank in player_wins.items() if rank == max_rank]
    return winners

if check==False:
    straight_flush()

def four_of_a_kind():
    global check
    result_card_dic()
    only_numerics()

    four_of_a_kind_players = {}

    for player, cards in only_numerics().items():
        for i in range(len(cards) - 3):
            if cards[i] == cards[i + 1] == cards[i + 2] == cards[i + 3]:
                four_of_a_kind_players[player] = cards[i:i + 4]
                break

    if not four_of_a_kind_players:
        return "No four of a kind found."

    try:
        max_rank = max(cards[0] for cards in four_of_a_kind_players.values())
    except:
        pass

    winners = [player for player, cards in four_of_a_kind_players.items() if cards[0] == max_rank]

    check=True
    if len(winners) > 1:
        return f"Winners: {', '.join(winners)}"
    else:
        return f"Winner: {winners[0]}"

if check==False:
    four_of_a_kind()

def Full_house():
    global check
    result_card_dic()
    only_numerics()   
    pairs = {}
    final_winner={}
    for player,cards in only_numerics().items():
        triple = []
        double=[]
        for card in cards:
            count=cards.count(card)
            if count ==3:
                if card not in triple:
                    triple.append(card)
            if count ==2:
                if card not in double:
                    double.append(card) 

        if len(triple) ==1 and len(double) !=0:
            triple.append(double[0])
            pairs[player]=triple    
        elif len(triple)==2:
            pairs[player]=triple
    try:
        max_values =max(pairs.values())
    except:
        pass
    for player,cards in pairs.items():
        if cards[:2] == max_values[:2]:
            final_winner[player]=cards        
    check=True       
    
    return  final_winner

if check==False:
    Full_house()


def Flush():
    global check
    
    suits_dic = {}
    for player,cards in player_control_dic.items():
        new_list=[]
        for card in cards:
            new_list.append(card[-1])

        for suit in new_list:
            if new_list.count(suit)>4:

                rank_list=[]
                for card in cards:
                    if card[-1]==suit:
                        rank_list.append(card[:-1])
                suits_dic[player]=rank_list
    try:
        last_winner = max(cards[0] for cards in suits_dic.values())
    except:
        pass
        
    check = True
    return last_winner

if check==False:
    Flush()


def straight():
    global check
    result_card_dic()
    only_numerics()

    duzenli_ardisik_dict={}
    only_new_numeric={}
    for player, cards in only_numerics().items():
        
        uniq_cards=[]
        for i in range(len(cards)):
            
            if cards[i] not in uniq_cards:
                uniq_cards.append(cards[i])

        only_new_numeric[player] = uniq_cards 

    for player, cards in only_new_numeric.items():
        for i in range(len(cards) - 4):  
            if cards[i]==cards[i+4]+4 :
                duzenli_ardisik_dict[player]=cards[i:i+5]   
                break             

    
    winners={}
    for player,cards in duzenli_ardisik_dict.items():
        winners[player]=player_control_dic[player]
    check = True 

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
            for key,value in last_winner.items():
                if value == max(last_winner.values()):
                    last_winner[key]=value        
            
    except:
        pass
    
    return last_winner

if check==False:
    straight()

def three_of_a_kind():
    global check
    only_numerics()
    


def three_of_a_kind():
    global check
    player_control_dic = result_card_dic()
    winners = []
    highest_rank = 0
    get_card_rank()
    card_values = [card[:-1] for card in player_control_dic.values()]
    value_counts = {}
    for value in card_values:
        value_counts[value] = value_counts.get(value, 0) + 1
    for count in value_counts.values():
        if count == 3:
            for player, cards in player_control_dic.items():
                card_values = [card[:-1] for card in cards]
                value_counts = {}
                for value in card_values:
                    value_counts[value] = value_counts.get(value, 0) + 1
                    for value, count in value_counts.items():
                        if count == 3:
                            rank = get_card_rank(value)
                            if rank > highest_rank:
                                highest_rank = rank
                                winners = [player]
                            elif rank == highest_rank:
                                winners.append(player)
    def get_card_rank(value):
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return ranks.get(value, 0)
    check = True
    return winners

if check== False:
    three_of_a_kind()
    
def two_pair():
    global check
    result_card_dic()
    only_numerics()   
    
    pairs_dic= {}
        
    for player,cards in only_numerics().items():
        double=[]
        een=[]
        pair=[]
        for card in cards:
            count=cards.count(card)
            if count ==2:
                if card not in double:
                    double.append(card)
            if count == 1:
                if card not in een:
                    een.append(card)
        if len(double)>=2:
            pair.extend(double[:2])
            pair.append(een[0])
            pairs_dic[player] = pair
    final_winner={} 
    try:
        for player,cards in pairs_dic.items():        
                    
            if cards == max(pairs_dic.values()):
                final_winner[player]=cards
                
    except:
        pass
        
    check = True	
    return  final_winner


if check == False:
    two_pair()
    
def one_pair():
    global check
    result_card_dic()
    only_numerics()
    finally_winner={}
    one_pairs_dict={}


    only_pair={}
    for player,cards in only_numerics().items():
        for card in cards:
            if len(set(cards))==6:
                if cards.count(card)==2 and player not in one_pairs_dict:
                    one_pairs_dict[player] = cards
                    only_pair[player]=card
    try:
        max_values=max(one_pairs_dict.values())
        for player,cards in one_pairs_dict.items():
            if cards[:6] == max_values[:6]:
                finally_winner[player]=cards
    except:
        pass
    check = True
    return finally_winner

if check == False:
    one_pair()

def high_card():
    global check
    result_card_dic()
    only_numerics()

    finally_winner = {}
    try:
        max_values =max(only_numerics().values())
        for player,cards in only_numerics().items():
            if cards[:5] == max_values[:5]:
                finally_winner[player] = cards
    except:
        pass
    check = True
    return finally_winner
