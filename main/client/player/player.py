import questionary
import random

cpu_names = ["CPU-RusselBeerMag", "CPU-Mr.Wes", "CPU-Chella", "CPU-Jade"]

class Player:

    def __init__(self, dums):
        """
        * Player constructor.

        * Initializes the variables:
        * points: the number of rounds won.
        * deck: the players deck of cards.
        * name: the name of the player.
        * has_valid_card: whether the player has a valid card.
        * dums: the class that runs the game.

        Args:
            dums (class): the class that runs the game.
        """ 
        self.dums = dums
        self.points = 0
        self.deck = []
        self.name = self.set_player_name()
        self.has_valid_card = True
        self.total_count = 0
        self.last_card = ()


    def __str__(self):
        return f"Name: {self.name}, Points: {self.points}, Deck: {self.deck}"    


    def set_player_name(self):
        """
        * Prompts the user for the name of the player

        Returns (str): Player name.
        """  
        name = str(input("Enter your name: "))
        while not name.isalnum():
            name = str(input("Enter your name: "))
        return name     
        

    def play_card(self):
        """
        Play a card from the player's deck.

        Args:
            player: Player object representing the player.
        """
        game_board = self.dums.game.game_board
        dums = self.dums

        card_to_play = self.choose_card_to_play()
        while(dums.is_valid_card(card_to_play, dums.left_end, dums.right_end) == False):
            card_to_play = self.choose_card_to_play()

        if not game_board:
            game_board.append(card_to_play)
        elif dums.can_play(card_to_play, True) and not dums.can_play(card_to_play, False):
            dums.play_card_on_board(card_to_play, True)
        elif dums.can_play(card_to_play, False) and not dums.can_play(card_to_play, True):
            dums.play_card_on_board(card_to_play, False)
        else:
            self.choose_side_to_play(card_to_play)
        self.deck.remove(card_to_play)


    def choose_card_to_play(self):
        """
        * Prompt the player to choose a card from their deck of cards.

        Returns:
            card_to_play (tuple): card chosen from the deck of cards.
        """        
        choices = [f"{card[0]}-{card[1]}" for card in self.deck]
        card_to_play = questionary.select("Choose a card:", choices=choices).ask()
        card_to_play = tuple(map(int, card_to_play.split("-")))
        return card_to_play  
    

    def choose_side_to_play(self, card):
        """
        Prompt the user to choose which end of the board they want to place their card.

        Args:
            card (tuple): Card to be played.
        """
        game_board = self.dums.game.game_board
        dums = self.dums

        selected_side = self.prompt_side_choice()
        flipped_card = dums.flip_card(card, selected_side == "left")
        if selected_side == "left":
            game_board.insert(0, flipped_card)
        else:
            game_board.append(flipped_card)


    def prompt_side_choice(self):
        """
        Prompt the player to choose a side to place their card.

        Returns:
            str: "left" or "right"
        """
        side_choices = ["left", "right"]   
        selected_side = questionary.select("Choose a side to place your card:", choices=side_choices).ask()
        return selected_side


    def set_player_deck(self,deck):
        """
        * setter method.
        * Sets the players deck of cards.

        Args:
            deck (list): a deck of cards.
        """        
        self.deck = deck    


class CPUPlayer(Player):

    def __init__(self, dums):
        super().__init__(dums)


    def choose_card_to_play(self):
        """
        Choose a card from the CPU player's deck randomly.

        Returns:
            card_to_play (tuple): card chosen from the deck of cards.
        """
        return random.choice(self.deck)


    def prompt_side_choice(self):
        """
        Choose a side to place the card for the CPU player.

        Returns:
            str: "left" or "right"
        """
        return random.choice(["left", "right"])
    

    def set_player_name(self):
        """
        Selects and removes a random name from a list of names for the CPU player.

        Returns (str): CPU player name.
        """
        player_name = random.choice(cpu_names)
        cpu_names.remove(player_name)
        return player_name