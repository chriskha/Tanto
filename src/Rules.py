'''
Created on Nov 30, 2012

@author: christopherkha
'''
from random import randrange, shuffle
from src.cards.EventCard import EventCard
from src.cards.LoveCard import LoveCard, LoveCard1
from src.cards.MaidCard import MaidCard

def createStartingDeck(town):
    deck = []
    
    for i in iter(town.loveCardsPile):
        if isinstance(i[0], LoveCard1):
            lovePile = i
    
    for _ in xrange(7):
        card = lovePile.pop()
        deck.append(card)
    
    for i in iter(town.chiefMaidsPile):
        if i[0].isChambermaid:
            startingMaidPile = i
        
    for _ in xrange(3):
        card = startingMaidPile.pop()
        deck.append(card)
        
    print "\nHAND CONTAINS: %d cards!" % (len(deck))
    print deck
    town.printall()
    return deck

def createStartingTown(town, cardList):
    genMaids = []
    for card in cardList:
        if isinstance(card, MaidCard):
            if card.maidType == 'Maid Chief':
                maidPile = []
                for _ in xrange(card.initialQuantity):
                    maidPile.append(card)
                town.chiefMaidsPile.append(maidPile)
            if card.maidType == 'General Maid':
                genMaids.append(card)
            if card.maidType == 'Private Maid':
                maidPile = []
                for _ in xrange(card.initialQuantity):
                    maidPile.append(card)
                town.privateMaidsPile.append(maidPile)
        elif isinstance(card, LoveCard):
            lovePile = []
            for _ in xrange(card.initialQuantity):
                lovePile.append(card)
            town.loveCardsPile.append(lovePile)
        elif isinstance(card, EventCard):
            eventPile = []
            for _ in xrange(card.initialQuantity):
                eventPile.append(card)
            town.eventCardsPile.append(eventPile)
    
    ''' Create Randomized 10 General Maids '''
    for _ in xrange(10):
        maidPile = []
        rn = randrange(0, len(genMaids))
        chosenMaid = genMaids[rn]
        for _ in xrange(chosenMaid.initialQuantity):
            maidPile.append(chosenMaid)
        genMaids.remove(chosenMaid)
        town.generalMaidsPile.append(maidPile)
        
    town.printall()
        
    shuffle(town.privateMaidsPile)
    for _ in xrange(2):
        card = town.privateMaidsPile.pop()
        town.privateMaidsUp.append(card)
    