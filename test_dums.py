import unittest
import dums
import io
import sys

sys.stdout = io.StringIO()

class MyTestCase(unittest.TestCase):
    def test_generate_dominoes(self):
        '''
        checks if the function generates a list of 28 dominoes(tuples)
        '''
        output = dums.generate_dominoes()
        self.assertEqual(len(output),28)
        self.assertIsInstance(output, list)
        self.assertEqual(all(output),True)

    def test_duplicate_dominoes(self):
        '''
        check for duplicate dominoes(tuples)
        '''
        dominoes = dums.generate_dominoes()
        self.assertEqual(all([dominoes.count(domino)==1 for domino in dominoes]),True)

    def test_shuffle_dominoes(self):
        '''
        checks if the function shuffled a list of 28 tuples
        '''
        output1 = dums.generate_dominoes()
        output2 = dums.shuffle_dominoes()
        self.assertEqual(len(output2),28)
        self.assertIsInstance(output2, list)
        self.assertEqual(all(output2),True)      
        self.assertNotEqual(output1, output2)

    def test_divide_dominoes(self):
        '''
        tests if the function evenly distributed the list of dominoes to the specified number of players
        '''     
        dominoes = dums.generate_dominoes()
        output1 = dums.divide_player_hands(dominoes,2)
        self.assertEqual(len(output1),2)
        self.assertIsInstance(output1, list)
        self.assertEqual(all(output1),True)

        dominoes = dums.generate_dominoes()
        output2 = dums.divide_player_hands(dominoes,4)
        self.assertEqual(len(output2),4)
        self.assertIsInstance(output2, list)
        self.assertEqual(all(output2),True)

        dominoes = dums.generate_dominoes()   
        dominoes.remove((0,0))
        output3 = dums.divide_player_hands(dominoes,3)
        self.assertEqual(len(output3),3)
        self.assertIsInstance(output3, list)
        self.assertEqual(all(output3),True)
        
    def test_play_card(self):
        '''
        TODO - test if the function makes it possible to play
        '''
        pass

    def test_klop(self):
        '''
        TODO - test if the function returns boolean
        '''
        ouputfalse = dums.klop([(0,0),(3,3)],[(5,2),(1,3)])
        ouputtrue = dums.klop([(0,0),(3,3)],[(5,2),(6,5)])
        self.assertEqual(ouputfalse,False)
        self.assertEqual(ouputtrue,True)


    def test_display_game(self):
        '''
        TODO - test if the function displays the current state of the game
        '''
        pass    

if __name__ == "__main__" :
    unittest.main()      