p_cards={'P1': ['JH', '10H'], 'P2': ['QD', 'KD'], 'P3': ['QC', '5H'], 'P4': ['3D', '3S'], 'P5': ['6D', '8H'], 'P6': ['5D', '10S']}
c_cards=['4H', 'AH', 'KH', 'QH', '9H']

one_pairs_dict={}
player_control_dic={}
finally_winner=[]

def result_card_dic():
    for i,j in p_cards.items():
            a=[]
            a.extend(j)
            a.extend(c_cards)
            player_control_dic[i]=a
    return player_control_dic

def straight():
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


# {'P1': [14, 13, 12, 11, 10, 9, 4],
#  'P2': [14, 13, 12,  9,  4],
#  'P3': [14, 13, 12,  9,  5, 4],
#  'P4': [14, 13, 12,  9,  4, 3]
#  'P5': [14, 13, 12,  9,  8, 6, 4],
#  'P6': [14, 13, 12, 10,  9, 5, 4]}
    duzenli_ardisik_dict={}
    
    for player, cards in only_numeric.items():
        
        uniq_cards=[]
        for i in range(len(cards)):
            
            if cards[i] not in uniq_cards:
                uniq_cards.append(cards[i])

        only_numeric[player] = uniq_cards 
# Cift kartlar teke indirildi

    for player, cards in only_numeric.items():
        for i in range(len(cards) - 4):  
            if cards[i]==cards[i+4]+4 :
                duzenli_ardisik_dict[player]=cards[i:i+5]   
                break             
            
# Ardisik olan kartlar bulundu

    finally_winner={}         
    for key,value in duzenli_ardisik_dict.items():
        if value == max(duzenli_ardisik_dict.values()):
            finally_winner[key]=value
            
    if len(finally_winner) > 1:
        return f"Kazananlar {finally_winner}"
    
    else:
        return f"Kazanan {finally_winner}"
#   BERABERLIK VE TEK KAZANAN DURUMLARI BELIRLENDI 
                            
print(straight())
