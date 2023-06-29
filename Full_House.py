p_cards={'P1': ['JH', 'JH'], 'P2': ['QD', 'AD'], 'P3': ['JC', '5H'], 'P4': ['3D', '3S'], 'P5': ['6D', '8H'], 'P6': ['5D', '10S']}
c_cards=['JH', 'AH', 'AH', 'QH', 'QH']


player_control_dic={}
winner_list=[]
values={}
def result_card_dic():
    for i,j in p_cards.items():
            a=[]
            a.extend(j)
            a.extend(c_cards)
            player_control_dic[i]=a
    return player_control_dic
def card_numeric():
    for player,cards in player_control_dic.items():
        list=[]
        for card in cards:
            if card[0]=="A":
                list.append(14)

            elif card[0]=="K":
                list.append(13)

            elif card[0]=="Q":
                list.append(12)

            elif card[0] =="J":
                list.append(11)
            else:
                list.append(int(card[0]))

        list.sort(reverse=True)
        values[player]=sorted(list,reverse=True)
    return values

#final_cards=result_card_dic()
#print(final_cards)

def Full_house():
    result_card_dic()
    card_numeric()

    pairs={}

    for player,cards in values.items():

        triple = []
        double=[]
        for i in range(1,(len(cards)-1) ):
            if cards[i]==cards[i-1] and cards[i]==cards[i+1]:
                    triple.append(cards[i])
                    i += 1
            elif cards[i]==cards[i-1] :
                double.append(cards[i])

        if len(triple) ==1 and len(double) !=0:
            pairs[player]=cards

    for player,cards in pairs.items():
        final_winner={}
        if cards == max(pairs.values()):
            final_winner[player]=cards

        if len(final_winner) > 1:
            return f"Winners {final_winner}"

        else:
            return f" Winner  {final_winner}"


    return  final_winner
sonuc=Full_house()
print(sonuc)
