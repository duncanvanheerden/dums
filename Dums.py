from main.setup.Game import Game
from pprint import pprint
import shutil
import questionary

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

class Dums():
    """
    This class represents the gameplay of the dums game.
    """

    def __init__(self):
        """
        Initialize the Dums class.
        """
        self.game = Game(self)
        self.left_end = None
        self.right_end = None
            

    def rungame(self):
        """
        Run the dums game.
        """   
        self.check_game_win()
        while not self.game.game_win: # Game is not won, play round
            self.game.setup_game()
            print("score limit:", self.game.score_limit)
            print("round:", self.game.round)
            self.play_round()
            self.check_game_win()


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
            return True
        elif card[0] in (left_side, right_side) or card[1] in (left_side, right_side):
            return True
        else: 
            return False


    def check_game_win(self):
        """
        Check if a player has won enough rounds to win the game.
        """
        for value in self.game.players:
            player = self.game.players[value]
            if player.wins >= self.game.score_limit:
                self.set_game_winner(player)
                # print(CLEAR, CLEAR_AND_RETURN)
                self.center_text(f"{self.get_game_winner().name} has won the game")
                self.game.game_win = True


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
            player.play_card()
            self.update_ends(False)
            return True
        else:
            print(f"{player.name} has klopped!!!")
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
        

    def check_round_win(self):
        """
        Check if the player has won the current round.

        Args:
            player: Player object representing the player.

        Returns:
            bool: True if the player has won the round, False otherwise.
        """
        # tell_game_win, tell_game_winner = self.lowest_total_win_case(self.game.players) 
        # if tell_game_win and all(not self.able_to_play(self.game.players[value]) for value in self.game.players):
        #     tell_game_winner.wins += 2
        #     return True
        # elif not tell_game_win and all(not self.able_to_play(self.game.players[value]) for value in self.game.players):
        #     return False
        for value in self.game.players:
            player = self.game.players[value]
            if len(player.deck) == 0:
                self.set_round_winner(player)
                player.wins += 1
                self.game.round += 1
                self.game.round_win = True


    def display_gameboard(self):
        """
        Display the current state of the game board.
        """
        self.center_text(f"LEFT --> {self.game.game_board} <-- RIGHT")


    def set_game_winner(self, player):
        """
        Sets the winner of the game.

        Args:
            player (object): Player that has won the game.
        """        
        self.game.game_winner = player


    def get_game_winner(self):
        """
        Returns:
            player (object): The winner of the game.
        """   
        return self.game.game_winner


    def set_round_winner(self, player):
        """
        Sets the winner of the round.

        Args:
            player (object): Player that has won the round.
        """  
        self.game.round_winner = player


    def get_round_winner(self):
        """
        Returns:
            player (object): The winner of the round.
        """       
        return self.game.round_winner


    def play_round(self):
        """
        Play a round of the game.
        """
        self.check_round_win()
        while self.game.round_win == False:
            for value in self.game.players:
                player = self.game.players[value]
                self.display_gameboard()
                print(f"{player.name}'s turn, Points = {player.wins}")
                self.handle_play(player)
                self.check_round_win()
                if self.game.round_win == True:
                    print(self.center_text(f"{player.name} Wins the round, Points = {self.get_round_winner().wins}"))
                    break
                # elif self.lowest_total_win_case(self.game.players)[0] == False:
                #     break
        self.update_ends(True)
        self.game.round_win = False        


if __name__ == '__main__':
    Dums().rungame()
