CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

class Rules():

    def __init__(self):
        self.won = True


    def valid_move(self):
        pass

    def able_to_play(game,player_deck):
        '''
        TODO - returns a boolean:
        * True if player cannot play a card.
        * False if player can play a card.
        '''
        list_of_bools = []
        leftside,rightside = game[0],game[-1]
        for card in player_deck:
            if card[0] != leftside[0] and card[0] != rightside[1] and card[1] != leftside[0] and card[1] != rightside[1]:
                list_of_bools.append(True) 
            else:
                list_of_bools.append(False) 
        if all(list_of_bools):  
            return True
        else:
            return False        
            

    def tell_game():
        '''
        TODO - tell game/ see who has the lowest number by counting player cards
        '''
        print('TELL GAME!')
        pass


    def round_won(self,player_deck):
        """
        * checks if a player has won the round,
        * by being the first to play all cards from their deck.
        """ 
        pass     