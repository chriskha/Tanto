'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src import rules

class Player(object):
    '''
    classdocs
    '''
    love_count = 0
    employ_count = 0
    service_count = 0

    def __init__(self, game):
        '''
        Constructor
        '''
        self.hand = []
        self.deck = []
        self.discard_pile = []
        self.play_field = []
        self.private_chamber = []
        self.love_count = 0
        self.employ_count = 1
        self.service_count = 1
        self.game = game
        
    def setup_player(self, town):
        self.deck = rules.create_starting_deck(town)
        self.employ_count = 1
        self.service_count = 1
        
    def draw_card(self, count=1):
        for _ in xrange(count):
            drawn_card = self.deck.pop()
            self.hand.append(drawn_card)
    
    def reset_turn(self):
        self.love_count = 0
        self.employ_count = 1
        self.service_count = 1
        
    