import random

class Game:


    def __init__(self):
        """
        * Game constructor.

        * Initializes the variables:
        * cards: list of shuffled cards.
        * board: list of cards played.
        * players_and_cards: dictionary of Key = players and Value = cards.
        * score_limit: maximum score.
        * round: number of rounds.
        """        
        self.cards = self.shuffle_cards()
        self.board = []
        self.players_and_cards = {}
        self.score_limit = 1
        self.round = 1


    @staticmethod
    def generate_cards():
        """
        * Generate the domino cards as a list of tuples.

        Returns:
            list: domino cards
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
        cards = self.cards

        all_hands = []
        while len(cards)>0:
            hand = []
            while len(hand)!=(len(cards)//num_players):
                card = cards[0]
                hand.append(card)
                cards.pop(0)
            else:
                all_hands.append(hand)  
        return all_hands  


    def choose_mode(self, num_of_players):
        """
        * Let the user choose the number of players.

        Returns:
            list: divided cards for each player
        """        
        # this method should be updated and used in gui
        if num_of_players == 2:
            return self.divide_cards(2)
        elif num_of_players == 3:
            self.cards.remove((0, 0))
            return self.divide_cards(3)
        elif num_of_players == 4:
            return self.divide_cards(4)


    def get_first_to_play(self):
        """
        * Gets the first player to play.

        Returns:
            list: player with the (6,6) card.
        """ 
        for deck in self.cards:
            if deck.count((6.6))>0:
                return deck


    def set_play_order(self):
        """
        * Sets the play order as a dictionary.
        * Key: player (e.g., "Player 1")
        * Value: player cards
        """
        arranged_cards = self.arrange_player_order()
        for num, deck in enumerate(arranged_cards):
            player_key = "Player " + str(num + 1)
            self.players_and_cards[player_key] = deck

            
    def arrange_player_order(self):
        """
        * Arranges the the game cards, so that the first player is the player with the (6,6) card.
        * Eg. [[(6,6)],[(3,4)],[(2,1)],[(1,2)]]

        Returns:
            list: re-arranged list of player decks.
        """        
        player_1 = self.get_first_to_play()
        new_card_order = []
        new_card_order.append(player_1)
        for player_deck in self.cards:
            if player_deck != player_1:
                new_card_order.append(player_deck)
        return new_card_order


    def set_score_limit(self, num_of_rounds):
        """
        * The score limit is set by the host of the game.
        """        
        self.score_limit = num_of_rounds 