import random


class Game():
    def __init__(self):
        self.cards = self.shuffle_cards()

    @staticmethod
    def generate_cards():
        '''
        generates the dominoe cards as a list of tuples
        '''
        cards = []
        k = 0
        for i in range(k, 7):
            for j in range(k, 7):
                cards.append((i, j))
            k += 1

        return cards


    def shuffle_cards(self):
        '''
        shuffles the position of each card in the deck list
        '''
        cards = self.generate_cards()
        shuffled_cards = []
        while len(shuffled_cards) != 28:
            card = random.choice(cards)
            shuffled_cards.append(card)
            cards.remove(card)

        return shuffled_cards


    def divide_cards(self,dominoes,num_of_players):
        '''
        divide cards and return a list of the player_hands
        '''
        all_hands = []
        len_dum = len(self.cards)
        while len(dominoes)>0:
            hand = []
            while len(hand)!=len_dum//num_of_players:
                card = dominoes[0]
                hand.append(card)
                self.cards.pop(0)
            else:
                all_hands.append(hand)  
        return all_hands 


    @staticmethod
    def choose_mode(self,dominoes):
        '''
        let user choose how many players
        '''
        num_of_players = None
    
        if num_of_players == "4":
            return self.divide_player_hands(dominoes,int(num_of_players))
        elif num_of_players == "3":
            dominoes.remove((0,0))
            return self.divide_player_hands(dominoes,int(num_of_players))
        elif num_of_players == "2":
            return self.divide_player_hands(dominoes,int(num_of_players))


    # def getFirstToPlay():
    #     '''
    #     TODO - decides who starts the game
    #     '''
    #     pass
