# from main.interface.Interface import Interface
from main.setup.Game import Game
from main.setup.rules import Rules
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

    def rungame(self):
        """
        * Run the dums game.
        """   
        
        while(self.check_win()==False): # boem is not won play round
            self.game.setup_game()
            print("score limit: ", self.game.score_limit)
            print("round: ", self.game.round)
            self.play_round()
            # stuff = input("say something: ")
            # if stuff.lower() == "quit": break
        # print("\n" + "Bye")

    
    def check_win(self):
        """
        * Checks if a player has won enough rounds to win the game.

        Returns:
            boolean: True if any player has won enough rounds to win the game, False otherwise.
        """
        for num in range(1, len(self.game.players) + 1):
            player = self.game.players[f"Player {num}"]
            if player.wins == self.game.score_limit:
                print(CLEAR,CLEAR_AND_RETURN)
                print(f"Player {num} has won the game")
                return True
        return False


    @staticmethod
    def center_text(text):
        # Get the width of the terminal window
        terminal_width = shutil.get_terminal_size().columns

        # Calculate the left padding to center the text
        left_padding = (terminal_width - len(text)) // 2

        # Generate the centered text
        centered_text = " " * left_padding + text

        output = '\n' + centered_text + '\n'
        print(CLEAR)
        print(output)


    def play_round(self):
        """
        * handles each round of the game until the score limit is reached.
        """ 
        round_won = False

        while(round_won == False):  # the round is not won, keep playing
            for num in range(1, len(self.game.players) + 1):
                self.center_text(str(self.game.game_board)) 
                player = self.game.players[f"Player {num}"]
                print("wins", player.wins)
                choices = [f"{card[0]}-{card[1]}" for card in player.deck]  # Convert tuples to strings
                card_to_play = questionary.select("Choose a card:", choices=choices).ask()
                card_to_play = tuple(map(int, card_to_play.split("-")))  # Convert selected string back to a tuple
                self.game.game_board.append(card_to_play)
                player.deck.remove(card_to_play)
                if len(player.deck) == 0:
                    player.wins += 1
                    self.game.round += 1
                    print("wins", player.wins)
                    round_won = True
                    break
                print(CLEAR_AND_RETURN)       


 


if __name__ == '__main__':
    Play().rungame()