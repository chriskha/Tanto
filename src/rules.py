'''
Created on Nov 30, 2012

@author: christopherkha
'''
from random import randrange, shuffle
from src.cards import event_card, love_card, maid_card, base_set

def create_starting_deck(town):
    deck = []
    
    for i in iter(town.love_cards_pile):
        if isinstance(i[0], love_card.LoveCard1):
            love_pile = i
    
    for _ in xrange(7):
        card = love_pile.pop()
        deck.append(card)
    
    for i in iter(town.chief_maids_pile):
        if i[0].is_chambermaid:
            starting_maid_pile = i
        
    for _ in xrange(3):
        card = starting_maid_pile.pop()
        deck.append(card)
        
    shuffle(deck)
    return deck

def create_starting_town(town, card_list):
    #testing purposes, save card list
    global cardset
    cardset = card_list
    
    gen_maids = []
    for card in card_list:
        if isinstance(card, maid_card.MaidCard):
            if card.maid_type == 'Maid Chief':
                maid_pile = []
                for _ in xrange(card.initial_quantity):
                    maid_pile.append(card)
                town.chief_maids_pile.append(maid_pile)
            if card.maid_type == 'General Maid':
                gen_maids.append(card)
            if card.maid_type == 'Private Maid':
                maid_pile = []
                for _ in xrange(card.initial_quantity):
                    maid_pile.append(card)
                town.private_maids_pile.append(maid_pile)
        elif isinstance(card, love_card.LoveCard):
            love_pile = []
            for _ in xrange(card.initial_quantity):
                love_pile.append(card)
            town.love_cards_pile.append(love_pile)
        elif isinstance(card, event_card.EventCard):
            event_pile = []
            for _ in xrange(card.initial_quantity):
                event_pile.append(card)
            town.event_cards_pile.append(event_pile)
    
    ''' Create Randomized 10 General Maids '''
    for _ in xrange(10):
        maid_pile = []
        rn = randrange(0, len(gen_maids))
        chosen_maid = gen_maids[rn]
        for _ in xrange(chosen_maid.initial_quantity):
            maid_pile.append(chosen_maid)
        gen_maids.remove(chosen_maid)
        town.general_maids_pile.append(maid_pile)
        
#    town.print_all()
    ''' Shuffle Private Maid deck and draw two of them '''
    shuffle(town.private_maids_pile)
    for _ in xrange(2):
        card = town.private_maids_pile.pop()
        town.private_maids_up.append(card)
        
def create_test_deck(town):
    deck = []
    
    for i in iter(town.love_cards_pile):
        if isinstance(i[0], love_card.LoveCard1):
            love_pile = i
    
    for _ in xrange(7):
        card = love_pile.pop()
        deck.append(card)
    
    for i in iter(town.chief_maids_pile):
        if i[0].is_chambermaid:
            starting_maid_pile = i
        
    for _ in xrange(3):
        card = starting_maid_pile.pop()
        deck.append(card)
    
    for i in iter(town.general_maids_pile):
        deck.append(i.pop())    
    
        
    shuffle(deck)
    return deck
    
def create_test2_deck(town):
    deck = []
    
    for i in iter(town.love_cards_pile):
        if isinstance(i[0], love_card.LoveCard1):
            love_pile = i
    
    for _ in xrange(7):
        card = love_pile.pop()
        deck.append(card)
    
#    for i in iter(town.chief_maids_pile):
#        if i[0].is_chambermaid:
#            starting_maid_pile = i
#        
#    for _ in xrange(3):
#        card = starting_maid_pile.pop()
#        deck.append(card)
#    
#    for i in iter(town.general_maids_pile):
#        deck.append(i.pop())
    for card in cardset:
        if card.card_number == 9:
            maid = card
    
    for _ in xrange(3):
        deck.append(maid)
    
        
    shuffle(deck)
    return deck
    
