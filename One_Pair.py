p_cards={'P1': ['JH', '10H'], 'P2': ['QD', 'KD'], 'P3': ['QC', '5H'], 'P4': ['3D', '3S'], 'P5': ['6D', '8H'], 'P6': ['5D', '10S']}
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
    
# 'P1': [14, 13, 12, 11, 10, 9, 4],
# 'P2': [14, 13, -, 12, -, 9, 4],
# 'P3': [14, 13, -, 12,  9, 5, 4],
# 'P4': [14, 13, 12,  9,  4, -, 3],
# 'P5': [14, 13, 12,  9,  8, 6, 4],
# 'P6': [14, 13, 12, 10,  9, 5, 4]}
    only_pair={}
    for player,cards in only_numeric.items():
        for card in cards:
            if len(set(cards))==6:
                if cards.count(card)==2 and player not in one_pairs_dict:
                    one_pairs_dict[player] = cards
                    only_pair[player]=card
#SADECE TEK CIFTE SAHIP OYUNCULAR BULUNDU  one_pairs_dict
#SADECE SAHIP OLDUKLARI CIFT ile OLAN DICT  only_pair
    
    for player,cards in one_pairs_dict.items():
        if cards == max(one_pairs_dict.values()):
            finally_winner[player]=cards
    
    if len(finally_winner) > 1:
        return f"Kazananlar {finally_winner}"
    
    else:
        return f"Kazanan {finally_winner}"   
# BERABERLIK DURUMU VE ASIL KAZANAN BELIRLENDI 

print(one_pair())


