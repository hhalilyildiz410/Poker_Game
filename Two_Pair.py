p_cards={'P1': ['5H', 'QH'], 'P2': ['6H', 'AD'], 'P3': ['JC', '6H'], 'P4': ['3D', '3S'], 'P5': ['6D', '8H'], 'P6': ['5D', '10S']}
c_cards=['JH', 'AH', 'AH', '6H', 'QH']


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

def two_pair():
    result_card_dic()
    card_numeric()   
    
    pairs_dic= {}
        
    for player,cards in values.items():
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
    for player,cards in pairs_dic.items():        
                
        if cards == max(pairs_dic.values()):
            final_winner[player]=cards
            
        else:
            print('Two pair yok')
        
        
    return  final_winner
sonuc=two_pair()
print(sonuc)
