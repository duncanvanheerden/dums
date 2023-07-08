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
            

    def rungame(self):
        """
        Run the dums game.
        """   
        win = self.check_win()
        
        while not win: # Game is not won, play round
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


    @staticmethod
    def is_valid_card(card, left_side, right_side):
        """
        Checks if the card a player wants to place on the game board is valid.

        Args:
            card (tuple): card chosen by player.

        Returns: 
            bool: True if the card is valid, False otherwise.
        """
        if left_side == None and right_side == None:
            print("should still work")
            return True
        elif card[0] in (left_side, right_side) or card[1] in (left_side, right_side):
            print("should work")
            return True
        else: 
            print("what am i doing here")
            return False


    def check_win(self):
        """
        Check if a player has won enough rounds to win the game.

        Returns:
            boolean: True if any player has won enough rounds to win the game, False otherwise.
        """
        for value in self.game.players:
            player = self.game.players[value]
            if player.wins >= self.game.score_limit:
                # print(CLEAR, CLEAR_AND_RETURN)
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
        # print(CLEAR, CLEAR_AND_RETURN)
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
            flipped_card = self.flip_card(card, True)
            self.game.game_board.insert(0, flipped_card)
        else:
            flipped_card = self.flip_card(card, False)
            self.game.game_board.append(flipped_card)


    def play_card_on_board(self, card, play_left):
        """
        Play the card on the game board.

        Args:
            card (tuple): Card to be played.
            play_left (bool): True if playing to the left, False if playing to the right.
        """
        flipped_card = self.flip_card(card, play_left)
        if play_left:
            self.game.game_board.insert(0, flipped_card)
        else:
            self.game.game_board.append(flipped_card)


    def choose_card_to_play(self, player):
        """
        Prompt the player to choose a card from their deck of cards.

        Args:
            player (class): Player object representing the player.

        Returns:
            card_to_play (tuple): _description_
        """        
        choices = [f"{card[0]}-{card[1]}" for card in player.deck]
        card_to_play = questionary.select("Choose a card:", choices=choices).ask()
        card_to_play = tuple(map(int, card_to_play.split("-")))
        return card_to_play            


    def play_card(self, player):
        """
        Play a card from the player's deck.

        Args:
            player: Player object representing the player.
        """
        card_to_play = self.choose_card_to_play(player)
        while(self.is_valid_card(card_to_play, self.left_end, self.right_end) == False):
            card_to_play = self.choose_card_to_play(player)

        if not self.game.game_board:
            self.game.game_board.append(card_to_play)
        elif self.can_play(card_to_play, True) and not self.can_play(card_to_play, False):
            self.play_card_on_board(card_to_play, True)
        elif self.can_play(card_to_play, False) and not self.can_play(card_to_play, True):
            self.play_card_on_board(card_to_play, False)
        else:
            self.choose_side_to_play(card_to_play)
        player.deck.remove(card_to_play)


    def can_play(self, card, play_left):
        """
        Check if the card can be played on the specified side of the game board.

        Args:
            card (tuple): Card to be played.
            play_left (bool): True if checking the left side, False if checking the right side.

        Returns:
            bool: True if the card can be played on the specified side, False otherwise.
        """
        side = self.left_end if play_left else self.right_end
        return card[0] == side or card[1] == side


    def flip_card(self, card, play_left):
        """
        Flip the card based on the board end and the play direction.

        Args:
            card (tuple): Card to be flipped.
            play_left: True if playing to the left, False if playing to the right.

        Returns:
            tuple: Flipped card.
        """
        card_end_left = card[0]
        card_end_right = card[1]

        if play_left and card_end_left == self.left_end:
            return (card_end_right, card_end_left)
        elif not play_left and card_end_right == self.right_end:
            return (card_end_right, card_end_left)
        else:
            return (card_end_left, card_end_right)


    def handle_play(self, player):
        """
        Handle the player's turn and play a card if possible.

        Args:
            player: Player object representing the player.

        Returns:
            bool: True if the player was able to play a card, False otherwise.
        """
        if len(player.deck) == 1:
            player.last_card = player.deck[0]
        if self.able_to_play(player):
            self.play_card(player)
            self.update_ends(False)
            return True
        else:
            print(f"{player} has klopped!!!")
            self.update_ends(False)
            return False


    def update_ends(self, is_none):
        """
        Update the values of left_end and right_end based on the current state of the game board.
        """
        if is_none:
            self.left_end = None
            self.right_end = None
        else:
            self.left_end = self.game.game_board[0][0]
            self.right_end = self.game.game_board[-1][1]


    def set_sum_of_player_decks(self):
        """
        TODO: Add docstring
        """
        for player in self.game.players:
            player = self.game.players[player]
            for card in player.deck:
                player.total_count += card[0]+card[1]


    def lowest_total_win_case(self,players):
        self.set_sum_of_player_decks()
        player_totals = [players[value].total_count for value in players]
        min_total = min(player_totals)
        for player in self.game.players:
            player = self.game.players[player]
            if player_totals.count(min_total) > 1:
                return False,player
            elif min_total == player.total_count:
                return True,player


    def milo_win(self,player):
        """
        TODO: Add docstring
        """
        player_totals = []
        for player in self.game.players:
            player_totals.append(player.total_count)
        

    def check_round_win(self, player):
        """
        Check if the player has won the current round.

        Args:
            player: Player object representing the player.

        Returns:
            bool: True if the player has won the round, False otherwise.
        """
        tell_game_win, tell_game_winner = self.lowest_total_win_case(self.game.players) 
        if tell_game_win and all(not self.able_to_play(self.game.players[value]) for value in self.game.players):
            tell_game_winner.wins += 2
            return True
        elif not tell_game_win and all(not self.able_to_play(self.game.players[value]) for value in self.game.players):
            return False
        elif len(player.deck) == 0:
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
                elif self.lowest_total_win_case(self.game.players)[0] == False:
                    break
        self.update_ends(True)        


if __name__ == '__main__':
    Play().rungame()