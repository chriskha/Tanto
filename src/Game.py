'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src import phase, town
from src.cards import base_set, event_card, love_card
import json

class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
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
    
    def draw_card(self, player, count=1):
        for _ in xrange(count):
            player.draw_card()
        #self.updatePlayer(player)
        
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
        self.phase.next_phase()
        
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