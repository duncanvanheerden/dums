import unittest
import dums
import gameSetup
import io
import sys

sys.stdout = io.StringIO()

class MyTestCase(unittest.TestCase):

    def test_SortPlayOrder(self):
        player_hands = dums.divide_player_hands(dums.shuffle_dominoes(),2)
        first2play = dums.bus(player_hands)
        new_play_order = gameSetup.sort_play_order(player_hands, first2play)
        self.assertEqual(new_play_order[0], first2play)
        # player_hands = dums.divide_player_hands(dums.shuffle_dominoes(),3)
        # print(player_hands)
        # first2play = dums.bus(player_hands)
        # new_play_order = gameSetup.sort_play_order(player_hands, first2play)
        # self.assertEqual(new_play_order[0], first2play)
        player_hands = dums.divide_player_hands(dums.shuffle_dominoes(),4)
        first2play = dums.bus(player_hands)
        new_play_order = gameSetup.sort_play_order(player_hands, first2play)
        self.assertEqual(new_play_order[0], first2play)


    def test_milo(self):
        game = [(6,6),(1,0)] 
        milo_win = gameSetup.milo([(0,6)],game)   
        normal_win_not_milo = gameSetup.milo([(0,4)],game)
        klop = gameSetup.milo([(4,3)],game)
        self.assertTrue(milo_win)
        self.assertFalse(normal_win_not_milo)
        self.assertFalse(klop)

if __name__ == "__main__" :
    unittest.main()       