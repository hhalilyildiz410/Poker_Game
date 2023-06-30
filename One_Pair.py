p_cards={'P1': ['JH', '10H'],
         'P2': ['QD', 'KD'],
         'P3': ['QC', '5H'],
         'P4': ['3D', '3S'],
         'P5': ['6D', '8H'],
         'P6': ['AD', '10S']}
c_cards=['4H', 'AH', 'KH', 'QH', '9H']


player_control_dic={}
finally_winner={}
one_pairs_dict={}

def result_card_dic():
    for i,j in p_cards.items():
            a=[]
            a.extend(j)
            a.extend(c_cards)
            player_control_dic[i]=a
    return player_control_dic

# final_cards=result_card_dic()
# print(final_cards)

def one_pair():
    result_card_dic()
    
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
        ###############   HER OYUNCUNUN KARTLARI SAYISAL OLARAK YAZILDI#############
    # return only_numeric

    only_pair={}
    for player,cards in only_numeric.items():
        for card in cards:
            if len(set(cards))==6:
                if cards.count(card)==2 and player not in one_pairs_dict:
                    one_pairs_dict[player] = cards
                    only_pair[player]=card
#SADECE TEK CIFTE SAHIP OYUNCULAR BULUNDU  one_pairs_dict
#SADECE SAHIP OLDUKLARI CIFT ile OLAN DICT  only_pair
    max_values=max(one_pairs_dict.values())
    for player,cards in one_pairs_dict.items():
        if cards[:6] == max_values[:6]:
            finally_winner[player]=cards
    
    if len(finally_winner) > 1:
        return f"Kazananlar {[[i,p_cards[i]] for i in finally_winner.keys()]}"
    
    else:
        return f"Kazanan {[[i,p_cards[i]] for i in finally_winner.keys()]}"   
# BERABERLIK DURUMU VE ASIL KAZANAN BELIRLENDI 

print(one_pair())
