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


def get_input():
    '''
    gets input from the user
    '''
    user_input = input('Enter: ')
    while user_input == "":
        print('What did you say?')
        user_input = get_input()
    return user_input    


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


def bus():
    '''
    TODO - decides who starts the game
    '''
    pass


def play_card(player_hand,game):
    '''
    TODO - play selected card from player hand
    '''
    
    pass


def klop(game,player_hand):
    '''
    TODO - returns a boolean:
    * True if player cannot play a card 
    * False if player can play a card
    '''
    list_of_bools = []
    leftside,rightside = game[0],game[-1]
    for card in player_hand:
        if card[0] != leftside[0] and card[0] != rightside[1] and card[1] != leftside[0] and card[1] != rightside[1]:
            list_of_bools.append(True) 
        else:
            list_of_bools.append(False) 
    if all(list_of_bools):  
        print('KLOPP!')  
        return True
    else:
        return False        
        

def tell_game():
    '''
    TODO - tell game/ see who has the lowest number by counting player cards
    '''
    print('TELL GAME!')
    pass


def display_game(game):
    '''
    TODO - show the table/game and all cards played
    '''
    print(game)
    pass


def run_game():
    welcome_player()
    win = False
    game = []
    dominoes = shuffle_dominoes()    
    player_hands = choose_mode(dominoes)  
    while win != True: 
        for player_hand in range(len(player_hands)):
            player_hand = player_hands[player_hand]
            print(player_hand)
            if len(game)==0:
                play_card(player_hand,game)
            # you need to add a function to 
            if klop(game,player_hand) == False:
                game = play_card(player_hand,game)
            



if __name__ == '__main__':
    run_game()



