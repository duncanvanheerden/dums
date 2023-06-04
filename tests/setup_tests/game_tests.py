import sys
import os

# Add the main package path to the Python path
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))
sys.path.append(root_directory)

import unittest
from main.setup.Game import Game


class MyTestCase(unittest.TestCase):


    def test_shuffle_cards(self):
        game = Game()
        cards = game.shuffle_cards()
        self.assertEqual(len(cards), 28)  # Check if all cards are present
        self.assertEqual(len(set(cards)), 28)  # Check if all cards are unique


    def test_divide_cards(self):
        game = Game()
        decks = game.divide_cards(2)
        self.assertEqual(len(decks), 2)  # Check if the cards are divided into 2 player decks      
        self.assertEqual(len(decks[0]), 14)  # Check if each player deck has the correct number of cards


    def test_choose_mode(self):
        game = Game()
        game.choose_mode(4)
        self.assertEqual(len(game.player_decks), 4)  # Check if the player decks are created
        self.assertEqual(len(game.player_decks[0]), 7)  # Check if each player deck has the correct number of cards
        self.assertEqual(len(game.player_decks[3]), 7)


    def test_get_first_to_play(self):
        game = Game()
        game.choose_mode(4)
        first_player = game.get_first_to_play()
        self.assertTrue(first_player.count((6,6))>0)  # Check if the correct player deck is returned


    def test_set_player_dict(self):
        game = Game()
        game.cards = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)]
        game.player_decks = [[(0, 0), (1, 1), (2, 2)], [(3, 3), (4, 4), (5, 5)], [(6, 6), (0, 1), (0, 2)], [(0, 3), (0, 4), (0, 5)]]
        game.set_player_dict()

        expected_players = {
            "Player 1": [(6, 6), (0, 1), (0, 2)],
            "Player 2": [(0, 0), (1, 1), (2, 2)],
            "Player 3": [(3, 3), (4, 4), (5, 5)],
            "Player 4": [(0, 3), (0, 4), (0, 5)]}

        self.assertEqual(game.players, expected_players)


    def test_arrange_player_order(self):
        game = Game()
        game.choose_mode(4)
        arranged_decks = game.arrange_player_order()
        first_player = arranged_decks[0]
        self.assertTrue(first_player.count((6,6)), True)  # Check if the first player deck is the one with (6, 6)
        self.assertEqual(len(arranged_decks), 4)  # Check if all player decks are present


    def test_set_score_limit(self):
        game = Game()
        game.set_score_limit(5)
        self.assertEqual(game.score_limit, 5)  # Check if the score limit is set correctly


if __name__ == '__main__':
    unittest.main()
