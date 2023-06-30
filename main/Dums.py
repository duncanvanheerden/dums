# from main.interface.Interface import Interface
from setup.Game import Game
from setup.rules import Rules
from pprint import pprint
import shutil
import questionary

"""

This module will run the dums game

"""

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

class Play():

    def __init__(self):
        """
        * Initialize the game.
        """        
        # self.interface = Interface()
        self.game = Game()
        self.left_end = None
        self.right_end = None
        self.last_card_played = ()
            

    def rungame(self):
        """
        * Run the dums game.
        """   

        win = self.check_win()
        
        while(win==False): # boem is not won play round
            self.game.setup_game()
            print("score limit: ", self.game.score_limit)
            print("round: ", self.game.round)
            self.play_round()
            win = self.check_win()


    @staticmethod
    def has_valid_card(player, left_side, right_side):
        """
        Checks if the player has a card that can be played on either side of the game board.

        Args:
            player: Player object representing the player.
            left_side: Number on the left side of the game board.
            right_side: Number on the right side of the game board.

        Returns:
            bool: True if the player has a valid card, False otherwise.
        """
        return any(
            card[0] in (left_side, right_side) or card[1] in (left_side, right_side)
            for card in player.deck
        )


    def check_win(self):
        """
        * Checks if a player has won enough rounds to win the game.

        Returns:
            boolean: True if any player has won enough rounds to win the game, False otherwise.
        """
        for value in self.game.players:
            player = self.game.players[value]
            if player.wins == self.game.score_limit:
                # print(CLEAR,CLEAR_AND_RETURN)
                print(f"{value} has won the game")
                return True
        return False


    def able_to_play(self, player):
        """
        TODO - Returns a boolean:
        * True if player can play a card.
        * False if player cannot play a card.
        """
        if self.left_end is None or self.right_end is None:
            return True
        
        return self.has_valid_card(player, self.left_end, self.right_end)


    @staticmethod
    def center_text(text):
        # Get the width of the terminal window
        terminal_width = shutil.get_terminal_size().columns

        # Calculate the left padding to center the text
        left_padding = (terminal_width - len(text)) // 2

        # Generate the centered text
        centered_text = " " * left_padding + text

        output = '\n' + centered_text + '\n'
        # print(CLEAR,CLEAR_AND_RETURN)
        print(output)


    def choose_side_to_play(self,card):
        """
        * Prompts the user to choose which end of the board they want to pace their card.
        """  
        side_choices = ["left", "right"]   
        selected_side = questionary.select("Choose as side to place your card:", choices=side_choices).ask()
        if selected_side == "left":
            self.game.game_board.insert(0,card)
        else:
            self.game.game_board.append(card)    


    def play_card(self,player):
        choices = [f"{card[0]}-{card[1]}" for card in player.deck]  # Convert tuples to strings
        card_to_play = questionary.select("Choose a card:", choices=choices).ask()
        card_to_play = tuple(map(int, card_to_play.split("-")))  # Convert selected string back to a tuple
        if not self.game.game_board:
            self.game.game_board.append(card_to_play)
        else:   
            self.choose_side_to_play(card_to_play)
        player.deck.remove(card_to_play)


    def handle_play(self,player):
        if self.able_to_play(player) == True:
            self.play_card(player)
            self.left_end = self.game.game_board[0][0]
            self.right_end = self.game.game_board[-1][1]
            return True
        else:
            print(f"{player} has klopped!!!")
            self.left_end = self.game.game_board[0][0]
            self.right_end = self.game.game_board[-1][1]
            return False
        

    def check_round_win(self,player):
        if len(player.deck) == 0:
            player.wins += 1
            self.game.round += 1
            return True
        else: return False
            

    def display_gameboard(self):
        self.center_text(str(self.game.game_board))    


    def play_round(self):
        """
        * handles each round of the game until the score limit is reached.
        """ 
        round_win = False

        while(round_win == False):  # the round is not won, keep playing
            for value in self.game.players:
                player = self.game.players[value]   
                self.display_gameboard()
                print("Player wins: ", player.wins)
                self.handle_play(player)
                round_win = self.check_round_win(player)   
                if (round_win == True):
                    print("wins", player.wins)
                    break
                

if __name__ == '__main__':
    Play().rungame()