p_cards={'P1': ['JH', 'JH'], 'P2': ['QD', 'AD'], 'P3': ['JC', '5H'], 'P4': ['3D', '3S'], 'P5': ['6D', '8H'], 'P6': ['5D', '10S']}
c_cards=['4H', 'AH', 'AH', 'QH', '9H']

player_control_dic={}
winner_list=[]
def result_card_dic():
    for i,j in p_cards.items():
            a=[]
            a.extend(j)
            a.extend(c_cards)
            player_control_dic[i]=a
    return player_control_dic

#final_cards=result_card_dic()
#print(final_cards)

def two_pair():
    result_card_dic()
    pairs=[]
    values={}

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

        list.sort(reverse=True)
        values[player]=sorted(list,reverse=True)    

        pair_values = []

        for i in range(len(list)-1 ):
            if list[i]==list[i+1]:
                    pair_values.append(list[i])
        if len(pair_values) == 2:
            pairs.append((player, pair_values))
    j=1
    en=pairs[0][1]
    for j in range(len(pairs)-1):
        if pairs[j][1] > en or pairs[j][1]==en :
            en=pairs[j][1]
            max=pairs[j]
            j+=1

    winner_list.append(max)

    return winner_list  
sonuc=two_pair()
print(sonuc)
