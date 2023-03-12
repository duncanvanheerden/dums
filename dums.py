import inquirer
import random
import gameSetup

cards_played = []
def welcome_player():
    '''
    prints the welcome message
    '''
    print('''
==================================================
==                                              ==
|   #######    ###    ### ##      ##  #######    |
|   ##    ###  ##      ## ###    ### ##     ##   |
|   ##      ## #        # #  #  #  #  ###___     |
|   ##      ## ##      ## #   ##   #      ###    |
|   ##    ###  ###    ### ##      ## ##     ##   |
|   #######      ######   ###    ###  #######    |
==                                              ==
==================================================
''') 


def generate_dominoes():
    '''
    generates the dominoe cards as a list of tuples
    '''
    dominoes = []
    k = 0
    for i in range(k,7):    
        for j in range(k,7):
            dominoes.append((i,j))
        k+=1   
    return dominoes  


def shuffle_dominoes():
    '''
    shuffles the position of each card in the dums list
    '''
    cards = generate_dominoes()
    shuffled_cards = []
    while len(shuffled_cards)!=28:
        card = random.choice(cards)
        shuffled_cards.append(card)
        cards.remove(card)
    return shuffled_cards


def divide_player_hands(dominoes,num_of_players):
    '''
    divide cards and return a list of the player_hands
    '''
    all_hands = []
    len_dum = len(dominoes)
    while len(dominoes)>0:
        hand = []
        while len(hand)!=len_dum//num_of_players:
            card = dominoes[0]
            hand.append(card)
            dominoes.pop(0)
        else:
            all_hands.append(hand)  
    return all_hands        
        

def choose_mode(dominoes):
    '''
    let user choose how many players
    '''
    player_input = [inquirer.List("mode",message="How many players? " ,choices=["2","3","4"],)]
    num_of_players = inquirer.prompt(player_input)['mode']
    if num_of_players == "4":
        return divide_player_hands(dominoes,int(num_of_players))
    elif num_of_players == "3":
        dominoes.remove((0,0))
        return divide_player_hands(dominoes,int(num_of_players))
    elif num_of_players == "2":
        return divide_player_hands(dominoes,int(num_of_players))


def bus(all_hands):
    '''
    TODO - decides who starts the game
    '''
    for player,dominoes in enumerate(all_hands):
        for dominoe in dominoes:
             if dominoe == (6,6):
                return all_hands[player]

def get_player_card(player_hand):
    player_input = [inquirer.List("played",message="Pick a card to play.",choices=[str(card) for card in player_hand],)]
    card = inquirer.prompt(player_input)['played']
    return int(card[1]),int(card[4])


def play_card(player_hand,game):
    '''
    TODO - play selected card from player hand
    '''
    user_card = get_player_card(player_hand)
    while  user_card not in player_hand and is_valid_move(game,user_card) == False:
        user_card = get_player_card(player_hand)
        if is_valid_move(game,user_card)==False:
            print('that is not a valid move')
    
    cards_played.append(user_card[0])
    cards_played.append(user_card[1])
    return user_card


def klop(game,player_hand,player_num):
    '''
    TODO - returns a boolean:
    * True if player cannot play a card 
    * False if player can play a card
    '''
    list_of_bools = []
    if len(game)>=1:
        leftside,rightside = game[0][0],game[-1][1]
        for card in player_hand:
            if card[0] != leftside and card[0] != rightside and card[1] != leftside and card[1] != rightside:
                list_of_bools.append(True) 
            else:
                list_of_bools.append(False) 
        if all(list_of_bools):  
            print(f'PLAYER {player_num+1} : KLOPP!')  
            return True
        else:
            return False    
    else:
        return False    


def get_end_cards(game):
    """_summary_

    Args:
        game (list): current state of game/cards_played
    """    
    leftside,rightside = game[0],game[-1]
    return(leftside,rightside)

def is_valid_move(game,card):
    """_summary_

    Args:
        game (_type_): _description_
        card (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if len(game)>1:
        print(game)
        leftside,rightside = game[0][0],game[-1][1]
        if card[0] != leftside and card[0] != rightside and card[1] != leftside and card[1] != rightside:
            print(card)
            return False
    else:
        return True
    

def tell_game():
    '''
    TODO - tell game/ see who has the lowest number by counting player cards
    '''
    end_cards = get_end_cards()
    if cards_played.count(end_cards[0]) == 7 and cards_played.count(end_cards[1])==7:
        print('It seems we have reached a game of calculations......')
        return True
    return False


def tell_game_rulling(all_hands):
    player_counts = []
    player_total = 0
    if tell_game():
        for hand in all_hands:
            for dominoes in hand:
                player_total+=(dominoes[0]+dominoes[1])
            player_counts.append(player_total)
        return player_counts.index(min(player_counts))

def update_player_scores(player_scores,player_num,points):
    """_summary_

    Args:
        player_scores (_type_): _description_
        player_num (_type_): _description_
        points (_type_): _description_

    Returns:
        _type_: _description_
    """    
    player_scores[f'player {player_num+1}'] +=points
    print(player_scores)


def set_score_limit()-> int:
    """
    prompts the user to set the score_limit

    Returns:
        int : score limit
    """
    player_input = [inquirer.List("boem",message="How many points to win? " ,choices=["1","2","3","4","5"],)]
    limit = inquirer.prompt(player_input)['boem']
    return int(limit)

def run_game():
    """_summary_
    """    
    welcome_player()
    win = False
    dominoes = shuffle_dominoes()    
    all_hands = choose_mode(dominoes) 
    first2play = bus(all_hands)
    player_hands = gameSetup.sort_play_order(all_hands,first2play)
    player_scores = {f'player {player+1}': 0 for player in range(len(player_hands))}
    score_limit = set_score_limit()
    game = [] 
    while win == False: 
        for player_num,player_hand in enumerate(player_hands):
            points = 0
            if klop(game,player_hand,player_num) == False:
                if len(game)>1:
                    leftside,rightside = game[0][0],game[-1][1]
                elif len(game) == 1:
                    leftside,rightside = game[0][0],game[0][1]  

                card = play_card(player_hand,game)
                if len(game)==0:
                    game.append(card)
                    player_hand.remove(card)
                elif len(game)<2:
                    if card[1]==rightside:
                        flipcard = card[1],card[0]
                        game.append(flipcard)
                    else:
                        game.append(card) 
                    player_hand.remove(card) 
                elif card[0]==leftside or card[1] == leftside:
                    if card[0]==leftside:
                        flipcard = card[1],card[0]
                        game.insert(0,flipcard)
                    else:
                        game.insert(0,card)    
                    player_hand.remove(card) 
                elif card[0]==rightside or card[1] == rightside:
                    if card[1]==rightside:
                        flipcard = card[1],card[0]
                        game.append(flipcard)
                    else:
                        game.append(card)    
                    player_hand.remove(card) 
                print(str(game).center(150))
            
            # elif gameSetup.milo(player_hand,game):
            #     points+=2
            #     break
            # elif tell_game_rulling(player_hands):
            #     points+=2
            #     break
            if len(player_hand)==0:
                points+=1
                break
        
    update_player_scores(player_scores,player_num,points)
    print(f'Player {player_num+1} wins!')        

if __name__ == '__main__':  
    run_game()    