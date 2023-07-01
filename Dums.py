from main.setup.Game import Game
from pprint import pprint
import shutil
import questionary

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

class Play():
    """
    This class represents the gameplay of the dums game.
    """

    def __init__(self):
        """
        Initialize the Play class.
        """
        self.game = Game()
        self.left_end = None
        self.right_end = None
        self.last_card_played = ()
            
    def rungame(self):
        """
        Run the dums game.
        """   
        win = self.check_win()
        
        while win == False: # Game is not won, play round
            self.game.setup_game()
            print("score limit:", self.game.score_limit)
            print("round:", self.game.round)
            self.play_round()
            win = self.check_win()

    @staticmethod
    def has_valid_card(player, left_side, right_side):
        """
        Check if the player has a card that can be played on either side of the game board.

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
        Check if a player has won enough rounds to win the game.

        Returns:
            boolean: True if any player has won enough rounds to win the game, False otherwise.
        """
        for value in self.game.players:
            player = self.game.players[value]
            if player.wins == self.game.score_limit:
                print(CLEAR, CLEAR_AND_RETURN)
                self.center_text(f"{value} has won the game")
                return True
        return False

    def able_to_play(self, player):
        """
        Check if the player can play a card.

        Returns:
            bool: True if the player can play a card, False otherwise.
        """
        if self.left_end is None or self.right_end is None:
            return True
        return self.has_valid_card(player, self.left_end, self.right_end)

    @staticmethod
    def center_text(text):
        """
        Center the text on the terminal window.

        Args:
            text (str): Text to be centered.
        """
        terminal_width = shutil.get_terminal_size().columns
        left_padding = (terminal_width - len(text)) // 2
        centered_text = " " * left_padding + text
        output = '\n' + centered_text + '\n'
        print(CLEAR, CLEAR_AND_RETURN)
        print(output)

    def choose_side_to_play(self, card):
        """
        Prompt the user to choose which end of the board they want to place their card.

        Args:
            card (tuple): Card to be played.
        """
        side_choices = ["left", "right"]   
        selected_side = questionary.select("Choose a side to place your card:", choices=side_choices).ask()
        if selected_side == "left":
            flipped_card = self.flip_card(card, self.left_end, True)
            self.game.game_board.insert(0, flipped_card)
        else:
            flipped_card = self.flip_card(card, self.right_end, False)
            self.game.game_board.append(flipped_card)

    def play_card(self, player):
        """
        Play a card from the player's deck.

        Args:
            player: Player object representing the player.
        """
        choices = [f"{card[0]}-{card[1]}" for card in player.deck]
        card_to_play = questionary.select("Choose a card:", choices=choices).ask()
        card_to_play = tuple(map(int, card_to_play.split("-")))
        if not self.game.game_board:
            self.game.game_board.append(card_to_play)
        elif self.can_play_left(card_to_play) and not self.can_play_right(card_to_play): 
            flipped_card = self.flip_card(card_to_play, self.left_end, True)
            self.game.game_board.insert(0, flipped_card)  
        elif self.can_play_right(card_to_play) and not self.can_play_left(card_to_play):
            flipped_card = self.flip_card(card_to_play, self.right_end, False)
            self.game.game_board.append(flipped_card)    
        else:   
            self.choose_side_to_play(card_to_play)
        player.deck.remove(card_to_play)

    def can_play_left(self, card):
        """
        Check if the card can be played on the left side of the game board.

        Args:
            card (tuple): Card to be played.

        Returns:
            bool: True if the card can be played on the left side, False otherwise.
        """
        left = self.left_end
        if card[0] == left or card[1] == left:
            return True
        else:
            return False

    def can_play_right(self, card):
        """
        Check if the card can be played on the right side of the game board.

        Args:
            card (tuple): Card to be played.

        Returns:
            bool: True if the card can be played on the right side, False otherwise.
        """
        right = self.right_end
        if card[0] == right or card[1] == right:
            return True
        else:
            return False

    def flip_card(self, card, board_end, play_left):
        """
        Flip the card based on the board end and the play direction.

        Args:
            card (tuple): Card to be flipped.
            board_end: End of the game board.
            play_left: True if playing to the left, False if playing to the right.

        Returns:
            tuple: Flipped card.
        """
        current_end_left = card[0]
        current_end_right = card[1]

        if play_left and current_end_left == self.left_end:
            return (current_end_right, current_end_left)
        elif not play_left and current_end_right == self.right_end:
            return (current_end_right, current_end_left)
        else:
            return (current_end_left, current_end_right)

    def handle_play(self, player):
        """
        Handle the player's turn and play a card if possible.

        Args:
            player: Player object representing the player.

        Returns:
            bool: True if the player was able to play a card, False otherwise.
        """
        if self.able_to_play(player):
            self.play_card(player)
            self.left_end = self.game.game_board[0][0]
            self.right_end = self.game.game_board[-1][1]
            return True
        else:
            print(f"{player} has klopped!!!")
            self.left_end = self.game.game_board[0][0]
            self.right_end = self.game.game_board[-1][1]
            return False

    def player_totals(self):
        """
        TODO: Add docstring
        """
        pass

    def win_round_at_both_ends(self):
        """
        TODO: Add docstring
        """
        pass

    def check_round_win(self, player):
        """
        Check if the player has won the current round.

        Args:
            player: Player object representing the player.

        Returns:
            bool: True if the player has won the round, False otherwise.
        """
        if len(player.deck) == 0:
            player.wins += 1
            self.game.round += 1
            return True
        else:
            return False

    def display_gameboard(self):
        """
        Display the current state of the game board.
        """
        self.center_text(f"LEFT --> {self.game.game_board} <-- RIGHT")

    def play_round(self):
        """
        Play a round of the game.
        """
        round_win = False

        while round_win == False:
            for value in self.game.players:
                player = self.game.players[value]
                self.display_gameboard()
                print("Player wins:", player.wins)
                self.handle_play(player)
                round_win = self.check_round_win(player)
                if round_win == True:
                    print("Wins:", player.wins)
                    break

if __name__ == '__main__':
    Play().rungame()
