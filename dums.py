import random
import dums_in_pygame.dums_pygame as pygame

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

def show_game_developments(game):
    for move in game:
        print(move,end=' ')

def play_card(player_hand,game):
    '''
    TODO - play selected card from player hand
    '''
    if len(game)>=2:
        leftside,rightside = game[0],game[-1]
    if klop(game,player_hand) == False:
        try:
            user_card = input('Please choose a card from your list of cards:')
            s = tuple(user_card.split(','))
            s =tuple(map(lambda a:int(a),s))
            if s in player_hand:
                cards_played.append(user_card)
                if len(game)<2: 
                    game.append(user_card)
                elif user_card[0] or user_card[1] == rightside:
                    game.insert(0,user_card)
                elif user_card[0] or user_card[1] == leftside:
                    game.append(user_card)
                show_game_developments(game)  
            elif tuple(user_card.split(',')) not in player_hand:
                
                print(s)
                print('Oops you do not have that card, But on the bright side.....you can still play this turn')
                play_card(player_hand,game)

        except ValueError:
            print('Please enter a valid card in this format:(upper card number,lower card number)')
            play_card(player_hand,game)

    else:
        klop(game,player_hand)

    


def klop(game,player_hand):
    '''
    TODO - returns a boolean:
    * True if player cannot play a card 
    * False if player can play a card
    '''
    list_of_bools = []
    if len(game)>=2:
        leftside,rightside = game[0],game[-1]
        for card in player_hand:
            if card[0] != leftside[0] and card[0] != rightside[1] and card[1] != leftside[0] and card[1] != rightside[1]:
                list_of_bools.append(True) 
            else:
                list_of_bools.append(False) 
        if all(list_of_bools):  
            print('KLOPP!')  
            return True
    elif len(game)<2:
        return False
    else:
        return False        


def get_end_cards(game):
    leftside,rightside = game[0],game[-1]
    return(leftside,rightside)



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



def display_game(game):
    '''
    TODO - show the table/game and all cards played
    '''
    print(game)
    pass


def run_game():
    pygame.pygame_window()
    welcome_player()
    win = False
    game = []
    dominoes = shuffle_dominoes()    
    player_hands = choose_mode(dominoes)  
    while win != True: 
        #start
        for player_hand in range(len(player_hands)):
            player_hand = player_hands[player_hand]
        print(player_hand)
        play_card(player_hand,game)
        # you need to add a function to 
        if klop(game,player_hand) == False:
            play_card(player_hand,game)
            continue
            



if __name__ == '__main__':
    run_game()



