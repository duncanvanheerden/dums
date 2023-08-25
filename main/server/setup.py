import random
import questionary
from collections import OrderedDict

from main.client.player import Player, CPUPlayer

class Game:


    def __init__(self, dums):
        """
        * Game constructor.

        * Initializes the variables:
        * cards: list of shuffled cards.
        * player_decks: list of player decks that consist of dominoe cards.
        * game_board: list of cards played.
        * players_and_cards: dictionary of Key = players and Value = cards.
        * score_limit: maximum score.
        * round: number of rounds.
        """  
        self.dums = dums      
        self.cards = self.shuffle_cards()
        self.player_decks = []
        self.game_board = []
        self.players = {}
        self.score_limit = 0
        self.round = 1
        self.game_win = False
        self.round_win = False
        self.round_winner = None
        self.game_winner = None


    @staticmethod
    def generate_cards():
        """
        * Generate the dominoe cards as a list of tuples.

        Returns:
            list: dominoe cards
        """       
        cards = []
        for i in range(7):
            for j in range(i, 7):
                cards.append((i, j))
        return cards


    def shuffle_cards(self):
        """
        * Shuffle the position of each card in the cards list.

        Returns:
            list: shuffled cards.
        """   
        cards = self.generate_cards()
        shuffled_cards = []
        while len(shuffled_cards)!=28:
            card = random.choice(cards)
            shuffled_cards.append(card)
            cards.remove(card)
        return shuffled_cards


    def divide_cards(self, num_players):
        """
        * Divide cards and return a list of player hands.

        Args:
            cards (list): the list of 28 game cards.
            num_players (int): the number of players in the game.

        Returns:
            list: all_player_decks
        """   
        copied_cards = [card for card in self.cards]
        all_player_decks = []
        while len(copied_cards)>0:
            deck = []
            while len(deck)!=(len(self.cards)//num_players):
                card = copied_cards[0]
                deck.append(card)
                copied_cards.pop(0)
            else:
                all_player_decks.append(deck)  
        return all_player_decks 


    def choose_mode(self, num_of_players):
        """
        * Let the user choose the number of players.

        Returns:
            list: divided cards for each player
        """        
        if num_of_players == 2:
            self.player_decks = self.divide_cards(2)
        elif num_of_players == 3:
            self.cards.remove((0, 0))
            self.player_decks = self.divide_cards(3)
        elif num_of_players == 4:
            self.player_decks = self.divide_cards(4)
 

    def get_first_to_play(self):
        """
        * Gets the first player to play.

        Returns:
            list: player with the (6,6) card.
        """ 
        for deck in self.player_decks:
            if deck.count((6,6))>0:
                return deck
    

    def set_player_dict(self):
        """
        * Sets the play order as a dictionary.
        * Key(num): player (e.g., "Player 1").
        * Value(deck): player deck.
        """
        arranged_cards = self.arrange_player_order() if self.round == 1 else self.player_decks
        players_list = ["Player"] + ["CPU"] * (len(arranged_cards) - 1)
        random.shuffle(players_list)
        
        for num, deck in enumerate(arranged_cards):
            player_key = f"Player {num + 1}"
            player = self.players.get(player_key)
            if player is None:
                player_type = Player if players_list[num] == "Player" else CPUPlayer
                player = player_type(self.dums)
                self.players[player_key] = player
            player.set_player_deck(deck)
        
            
    def arrange_player_order(self):
        """
        * Arranges the the game cards, so that the first player is the player with the (6,6) card.
        * Eg. [[(6,6)],[(3,4)],[(2,1)],[(1,2)]]

        Returns:
            list: re-arranged list of player decks.
        """        
        player_1_deck = self.get_first_to_play()
        new_deck_order = []
        new_deck_order.append(player_1_deck)
        for player_deck in self.player_decks:
            if player_deck != player_1_deck:
                new_deck_order.append(player_deck)
        return new_deck_order


    def set_score_limit(self, num_of_rounds):
        """
        * The score limit is set by the host of the game.
        """        
        self.score_limit = num_of_rounds 


    def setup_game(self):
        """
        Prompt the host to set up the game.
        """    
        if self.round == 1:
            player_num_opt = ["2","3","4"]
            score_limit_opt = ["1","2","3","4","5"]
            num_of_players = questionary.select("How many players (2-4):",choices=player_num_opt).ask()
            score_limit = questionary.select("Set the score limit (1-5):",choices=score_limit_opt).ask()
            self.choose_mode(int(num_of_players))
            self.set_score_limit(int(score_limit))
            self.set_player_dict()
        else:
            self.setup_new_round()
    

    def setup_new_round(self):
        """
        * Sets up a new round of the game.
        """  
        self.cards = self.shuffle_cards() 
        num_of_players =  len(self.players)
        self.player_decks = self.divide_cards(num_of_players)
        self.set_player_dict()
        self.players = OrderedDict(self.players)
        self.players.move_to_end(list(self.players.keys())[0])
        self.game_board = []
