'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src import Rules

class Player(object):
    '''
    classdocs
    '''
    loveCount = 0
    employCount = 0
    serviceCount = 0

    def __init__(self, game):
        '''
        Constructor
        '''
        self.hand = []
        self.deck = []
        self.discardPile = []
        self.playField = []
        self.privateChamber = []
        self.loveCount = 0
        self.employCount = 1
        self.serviceCount = 1
        self.game = game
        
    def setupPlayer(self, town):
        self.deck = Rules.createStartingDeck(town)
        self.employCount = 1
        self.serviceCount = 1
        
    def drawCard(self):
        drawnCard = self.deck.pop()
        self.hand.append(drawnCard)
    
    def resetTurn(self):
        self.loveCount = 0
        self.employCount = 1
        self.serviceCount = 1
        
    