'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src import phase, town
from src.cards import base_set, event_card, love_card, maid_card
from src.cards.love_card import LoveCard
from src.constants import STARTING_PHASE, SERVICE_PHASE, EMPLOY_PHASE
from src.phase import StartingPhase, ServicePhase
import json

class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._active_player = None
        self.town = town.Town()
        self.running = False
        self.phase = phase.PhaseManager(self, 
                                  (phase.StartingPhase(self), phase.ServicePhase(self), \
                                   phase.EmployPhase(self), phase.DismissPhase(self)),
                                  self.__entering_phase, self.__entered_phase, \
                                  self.__leaving_phase )
        
    def update(self):
        ''' Main game loop '''
        self.phase.update()
    
    def __entering_phase(self, phase):
        ''' Do something special for entering a phase, at the beginning of the phase '''
        pass
    
    def __entered_phase(self, phase):
        pass
    
    def __leaving_phase(self, phase):
        pass
    
    def setup_game(self, setup, players):
        set_list = read_json()
        card_set = build_card_set(set_list['cardList'])
        self.town.create_town(card_set)
        
        self.players = players
        players.setup_player(self.town)
        
        self.running = True
        self._active_player = players
        self.phase.next_phase()
        
    def draw_card(self, player, count=1):
        for _ in xrange(count):
            if len(player.deck) == 0:
                self.replenish_deck(player)
                
            '''If both Deck and Discard Pile are empty, don't draw anymore cards.'''
            if (len(player.deck)) == 0 and (len(player.discard_pile)) == 0:
                return
                
            player.draw_card()
        print "Hand: %s" % (player.hand)

        #self.updatePlayer(player)
        
    def replenish_deck(self, player):
        player.replenish_deck()
        
    def play_card(self, player, card):
        if self.phase == SERVICE_PHASE and not isinstance(card, maid_card.MaidCard):
            print "Can only play Maid Cards during SERVING PHASE!"
            return
        if self.phase == EMPLOY_PHASE and not isinstance(card, love_card.LoveCard):
            print "Can only play Love Cards during EMPLOY PHASE!"
            return
        if isinstance(card, maid_card.MaidCard):
            player.service_count -= 1
        
        print "\nPlayed card %s!" % card.name
        player.play_card(card)
        if self.phase == SERVICE_PHASE:
            card.serve_phase_played(self, player)
        elif self.phase == EMPLOY_PHASE:
            card.employ_phase_played(self, player)
        
            
        print "Love: %d, Services: %d, Employs: %d" % (player.love_count, player.service_count, player.employ_count)


    def buy_card(self, player, card_index):
        s = "%s" % (card_index+1)
        card_to_buy = self.town.town_set[s][0]
        if player.love_count >= card_to_buy.employ_cost:
            player.love_count -= card_to_buy.employ_cost
            player.employ_count -= 1
            card = self.town.town_set[s].pop()
            print card
            print self.town.general_maids_pile
            print self.town.town_set[s]
            player.discard_pile.append(card)
        else:
            print "Not enough love!"

    def discard_card_from_hand(self, player, card):
        player.discard_card_from_hand(card)
        
    def discard_all_from_hand(self, player):
        hand_size = len(player.hand)
        for _ in xrange(hand_size):
            player.discard_card_from_hand(player.hand[0])
            
    def discard_field_to_discard_pile(self, player):
        field_size = len(player.play_field)
        for _ in xrange(field_size):
            card = player.play_field[0]
            player.play_field.remove(card)
            player.discard_pile.append(card)
            
    def calculate_love(self, player):
        index = 0
        for _ in xrange(len(player.hand)):
            card = player.hand[index]
            if isinstance(card, LoveCard):
                self.play_card(player, card)
            else:
                index += 1
        
#move to Util.py ?
def read_json():
    fp = open("tanto_cuore.json", 'r')
    s = json.loads(fp.read())
    return s

def build_card_set(s):
    a = []
    for m in iter(s):
        if m == 'maid':
            for i in xrange(len(s[m])):
                b = base_set.get_maid_builder_func(s[m][i]['cardName'])
                #print s[m][i]['cardName']
                if b == None:
                    continue
                maid = b(s[m][i])
                a.append(maid)
        if m == 'love':
            for i in xrange(len(s[m])):
                b = love_card.get_love_builder_func(s[m][i]['cardName'])
                #print s[m][i]['cardName']
                if b == None:
                    continue
                love = b(s[m][i])
                a.append(love)
        if m == 'event':
            for i in xrange(len(s[m])):
                b = event_card.get_event_builder_func(s[m][i]['cardName'])
                #print s[m][i]['cardName']
                if b == None:
                    continue
                event = b(s[m][i])
                a.append(event)
    return a