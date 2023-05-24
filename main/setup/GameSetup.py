import random


class GameSetup():

    def __init__(self):
        self.cards = GameSetup.generateCards()
        pass


    def generateCards(numOfPlayers):
        '''
        generates the dominoe cards as a list of tuples
        '''
        cards = []
        k = 0
        for i in range(k,7):    
            for j in range(k,7):
                cards.append((i,j))
            k+=1   

        shuffeldDeck = GameSetup.shuffleCards(cards)

        return GameSetup.divideCards(shuffeldDeck,numOfPlayers)

         

    def shuffleCards(cards):
        '''
        shuffles the position of each card in the dums list
        '''
        cards = GameSetup.generate_dominoes()
        shuffled_cards = []
        while len(shuffled_cards)!=28:
            card = random.choice(cards)
            shuffled_cards.append(card)
            cards.remove(card)
        return shuffled_cards


    def divideCards(dominoes,num_of_players):
        '''
        divide cards and return a list of the player_hands
        '''
        all_hands = []
        len_dum = len(dominoes)
        while len(dominoes)>0:
            hand = []
            while len(hand)!=len_dum//num_of_players:
                card = dominoes[0]
                hand.append(card)
                dominoes.pop(0)
            else:
                all_hands.append(hand)  
        return all_hands        
            

    def choose_mode(dominoes):
        '''
        let user choose how many players
        '''
        num_of_players = None
         
        if num_of_players == "4":
            return GameSetup.divide_player_hands(dominoes,int(num_of_players))
        elif num_of_players == "3":
            dominoes.remove((0,0))
            return GameSetup.divide_player_hands(dominoes,int(num_of_players))
        elif num_of_players == "2":
            return GameSetup.divide_player_hands(dominoes,int(num_of_players))


    def getFirstToPlay():
        '''
        TODO - decides who starts the game
        '''
        pass
