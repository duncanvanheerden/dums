from main.setup.rules import Rules

class Player:

    def __init__(self):
        """
        * Player constructor.

        * Initializes the variables:
        * wins: the number of rounds won.
        * deck: the players deck of cards.
        * name: the name of the player.
        * has_valid_card: whether the player has a valid card.
        """  
        self.wins = 0
        self.deck = []
        self.name = ""
        self.has_valid_card = True
        self.total_count = 0
        self.last_card = ()
        

    def play_card(self,game_board):
        """
        * method to play card from deck.
        """ 
        pass

    

    
    def set_valid_card(self, able_to_play):
        """
        * setter method.
        * True if the player has a valid card to play.
        * False otherwise.

        Args:
            able_to_play (bool): boolean value indicating if the player is able to play.
        """      
        self.has_valid_card = able_to_play


    def set_player_deck(self,deck):
        """
        * setter method.
        * Sets the players deck of cards.

        Args:
            deck (list): a deck of cards.
        """        
        self.deck = deck    