'''
Created on Nov 29, 2012

@author: christopherkha
'''
from random import shuffle
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
#        self.deck = rules.create_starting_deck(town)
        self.deck = rules.create_test_deck(town)
        #self.deck = rules.create_test2_deck(town)
        self.draw_card(5)
        
#        print "\nCards in hand: %d" % (len(self.hand))
#        print self.hand
#        
#        print "\nDECK CONTAINS: %d cards!" % (len(self.deck))
#        print self.deck
        
        self.employ_count = 1
        self.service_count = 1
        
    def draw_card(self, count=1):
        for _ in xrange(count):
            drawn_card = self.deck.pop()
            self.hand.append(drawn_card)
            
    def replenish_deck(self):
        print "...Deck ran out...Replenishing deck..."
        l = len(self.discard_pile)
        print "Discard pile contains: %d cards." % (l)
        for _ in xrange(l):
            card = self.discard_pile[0]
            self.discard_pile.remove(card)
            self.deck.append(card)
        shuffle(self.deck)
        print "Deck has: %d cards" % (len(self.deck))
            
    def play_card(self, card):
        self.hand.remove(card)
        self.play_field.append(card)
        
    def discard_card_from_hand(self, card):
        self.hand.remove(card)
        self.discard_pile.append(card)
        print "\nDiscarded card %s" % (card.name)

    
    def reset_turn(self):
        self.love_count = 0
        self.employ_count = 1
        self.service_count = 1
        
    