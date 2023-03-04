import random

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
cards_played = []

def get_input():
    '''
    gets input from the user
    '''
    user_input = input('Enter: ')
    try:
        if user_input == "":
            print('What did you say?')
            get_input()
        else:
            return user_input 
    except ValueError:
        print('please enter a valid answer')
        get_input()

    

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
    print("How many players? (2/3/4)")
    num_of_players = get_input()
    while num_of_players.isalpha() or int(num_of_players) not in range(2,5):
        print("That's not a valid number! choose a different one.")
        num_of_players = get_input()  
    else:
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
                return player

# def show_game_developments(game):
#     fpri
def play_card(player_hand,game):
    '''
    TODO - play selected card from player hand
    '''
    
    if klop(game,player_hand) == False:
        try:
            user_card = input('Please choose a card from your list of cards:')
            s = tuple(user_card.split(','))
            b =tuple(map(lambda a:int(a),s))
            while  b not in player_hand and is_valid_move(game,b) == False:
                user_card = input('Please choose a card from your list of cards:')
                if b not in player_hand:
                     print('Oops you do not have that card, But on the bright side.....you can still play this turn')
                elif is_valid_move(game,b)==False:
                    print('that is not a valid move')
           
            cards_played.append(b[0])
            cards_played.append(b[1])
            return b

        except ValueError:
            print('Please enter a valid card in this format:(upper card number,lower card number)')
            play_card(player_hand,game)
    


    


def klop(game,player_hand):
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
            print('KLOPP!')  
            return True
        else:
            return False    
    else:
        return False    


def get_end_cards(game):
    leftside,rightside = game[0],game[-1]
    return(leftside,rightside)

def is_valid_move(game,card):
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

   
    if cards_played.count(end_cards[0]) == 7 or cards_played.count(end_cards[1])==7:
        print('It seems we have reached a game of calculations......')
        return True
    return False


def tell_game_ruling(all_hands):
    player_counts = []
    player_total = 0
    if tell_game():
        for hand in all_hands:
            for dominoes in hand:
                player_total+=(dominoes[0]+dominoes[1])
            player_counts.append(player_total)
        return player_counts.index(min(player_counts))





def run_game():
    welcome_player()
    win = False
    dominoes = shuffle_dominoes()    
    player_hands = choose_mode(dominoes) 
    game = [] 
    changed_game = []
    a =0
    while win != True: 
        #start
            if a > 3:
                a = 0
            player_hand = player_hands[a]
            print(f'\n{player_hand}')
            if len(game)>1:
                leftside,rightside = game[0][0],game[-1][1]
            b = play_card(player_hand,game)
            if len(game)<2: 
                game.append(b)
            elif b[0]==leftside or b[1] == leftside:
                game.insert(0,b)
            elif b[0]==rightside or b[1] == rightside:
                game.append(b)
            player_hand.remove(b) 
            # game.pop(game[-1])
            print(game)
            a+=1
            # you need to add a function to 
        
            



if __name__ == '__main__':
    run_game()




