p_cards={'P1': ['JH', '10H'], 'P2': ['QD', 'KD'], 'P3': ['QC', '5H'], 'P4': ['3D', '3S'], 'P5': ['6D', '8H'], 'P6': ['5D', '10S']}
c_cards=['4H', 'AH', 'KH', 'QH', '9H']
winner_set=set()
winner_list=[]
player_control_dic={}

def result_card_dic():
    for i,j in p_cards.items():
            a=[]
            a.extend(j)
            a.extend(c_cards)
            player_control_dic[i]=a
    return player_control_dic

# final_cards=result_card_dic()
# print(final_cards)

def royalflush():	
    result_card_dic()			
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
    print(winner_list)



def one_pair():
    result_card_dic()
    
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
        values[player]=sorted(list,reverse=True)
        ###############   HER OYUNCUNUN KARTLARI SAYISAL OLARAK YAZILDI#############
    # return values
    
# {'P1': [14, 13, 12, 11, 10, 9, 4],
#  'P2': [14, 13, 13, 12, 12, 9, 4],
#  'P3': [14, 13, 12, 12,  9, 5, 4],
#  'P4': [14, 13, 12, 9,   4, 3, 3],
#  'P5': [14, 13, 12, 9,   8, 6, 4],
#  'P6': [14, 13, 12, 10,  9, 5, 4]}    
    
    for player,cards in values.items():
        sayi=[]
        for card in cards:
            if cards.count(card)>1 and cards.count(card)<3:
                winner_list.append(player)
    for i in winner_list:
        if winner_list.count(i)<3:
            winner_set.add(i)
            
    return winner_set

