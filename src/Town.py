from random import random, randint, randrange
from src import Rules
from src.cards.EventCard import EventCard
from src.cards.LoveCard import LoveCard
from src.cards.MaidCard import MaidCard

class Town:
    def __init__(self):
        self.generalMaidsPile = []
        self.chiefMaidsPile = []
        self.privateMaidsPile = []
        self.privateMaidsUp = []
        self.loveCardsPile = []
        self.eventCardsPile = []
    
    def createTown(self, cardSet):
        Rules.createStartingTown(self, cardSet)

        
    def printall(self):
        for e in self.generalMaidsPile:
            print "GM %d of %s" % (len(e), e[0].__class__)
        for e in self.chiefMaidsPile:
            print "CM %d of %s" % (len(e), e[0].__class__)
        for e in self.privateMaidsUp:
            print "PM-UP %d of %s" % (len(e), e[0].__class__)
        for e in self.privateMaidsPile:
            print "PM-DN %d of %s" % (len(e), e[0].__class__)
        for e in self.loveCardsPile:
            print "LV %d of %s" % (len(e), e[0].__class__)
        for e in self.eventCardsPile:
            print "EV %d of %s" % (len(e), e[0].__class__)
        
