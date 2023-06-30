p_cards={'P1': ['KH', '10H'],
         'P2': ['QD', 'KD'],
         'P3': ['2C', 'KH'],
         'P4': ['3D', '3S'],
         'P5': ['6D', '8H'],
         'P6': ['5D', '10S']}
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

def high_card():
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

    max_values =max(only_numeric.values())
    for player,cards in only_numeric.items():
        if cards[:5] == max_values[:5]:
            finally_winner[player] = cards
    return finally_winner
#  en buyuk values i max() fonksiyonu ile max_values e atadim
# for dongusu ile sirayla value leri max_value ile kiyasladim.
#  eger value max_value ye esit ise finally_winnera ekledim
#  ilk 5 karti tamamen ayni ise berabere olarak kazananlar yazilir
print(high_card())
