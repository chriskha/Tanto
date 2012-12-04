'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src.constants import STARTING_PHASE, SERVICE_PHASE, EMPLOY_PHASE, \
    DISMISS_PHASE

class PhaseManager(object):
    ''' Handle entering/leaving the game phases '''
    def __init__(self, game, phases, enter_callback, entered_callback, end_callback):
        self.__game = game
        self.__phases = phases
        self.__enter_callback = enter_callback
        self.__entered_callback = entered_callback
        self.__end_callback = end_callback
        self.__current_phase = None
        
    def get_current_phase(self):
        return self.__current_phase
    
    def __eq__(self, other):
        return self.__current_phase.key == other
    
    def update(self):
        self.__current_phase.update()
        
    def next_phase(self):
        ''' Switch to next phase. If the current phase is the last one, go to the first '''
        if self.__current_phase == None:
            self.__current_phase = self.__phases[0]
        else:
            self.__end_callback(self.__current_phase)
            self.__current_phase.end_phase()
            
            try:
                self.__current_phase = (self.__phases)[self.__phases.index(self.__current_phase) + 1]
            except IndexError:
                self.__current_phase = (self.__phases)[0]
                
        self.__enter_callback(self.__current_phase)
        self.__current_phase.enter_phase()
        self.__entered_callback(self.__current_phase)
                
class Phase(object):
    '''
    A phase of the game
    '''


    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
        
    def enter_phase(self):
        pass
    
    def update(self):
        pass
    
    def end_phase(self):
        pass
    
class StartingPhase(Phase):
    name = "Starting Phase"
    key = STARTING_PHASE
    
    def enter_phase(self):
        print "Entering: %s" % (self.name)
        self.game._active_player.reset_turn()
        p = self.game._active_player
        print "Love: %d, Services: %d, Employs: %d\n" % (p.love_count, p.service_count, p.employ_count)
    
    def update(self):
        self.game.phase.next_phase()
            
    def end_phase(self):
        pass
    
class ServicePhase(Phase):
    name = "Serving Phase"
    key = SERVICE_PHASE
    
    def enter_phase(self):
        print "Entering: %s" % (self.name)
        p = self.game._active_player
        print "Love: %d, Services: %d, Employs: %d\n" % (p.love_count, p.service_count, p.employ_count)
    
    def update(self):
        if self.game._active_player.service_count == 0:
            self.game.phase.next_phase()
        else:
            make_decision(self.game, self.game._active_player, self.game._active_player.hand, "play")
        
    def end_phase(self):
        pass
    
class EmployPhase(Phase):
    name = "Employ Phase"
    key = EMPLOY_PHASE
    
    def enter_phase(self):
        print "Entering: %s" % (self.name)
        p = self.game._active_player
        print "Love: %d, Services: %d, Employs: %d\n" % (p.love_count, p.service_count, p.employ_count)
    
    def update(self):
        if self.game._active_player.employ_count == 0:
            self.game.phase.next_phase()
        else:
            make_decision(self.game, self.game._active_player, self.game._active_player.hand, "play")
    
    def end_phase(self):
        pass
    
class DismissPhase(Phase):
    name = "Dismiss Phase"
    key = DISMISS_PHASE
    
    def enter_phase(self):
        print "Entering: %s" % (self.name)
        p = self.game._active_player
        print "Discarding Hand and Play_field to Discard Pile"
        self.game.discard_all_from_hand(p)
        self.game.discard_field_to_discard_pile(p)
        print "Discard Pile contains: %d cards." % (len(p.discard_pile))
    
    def update(self):
        self.game.phase.next_phase()
                
    def end_phase(self):
        game = self.game
        player = game._active_player
        print "Draw new hand!"
        game.draw_card(player, 5)
        print "Cards left in Deck: %d" % (len(player.deck))
    
    
def make_decision(game, player, pile, action):
    print "%s" % (game.phase.get_current_phase().name)
    print "Make a decision. Input number to %s card from hand. Press <Enter> for no action." % (action)
    index = 1
    for card in pile:
        print "%d - %s" % (index, card.name)
        index += 1
        
    inp = raw_input("Choice: ")
    if inp == "":
        inp = -1
    else:
        inp = int(inp) - 1

    if inp >= 0 and inp < index-1:
        if action == "play":
            game.play_card(player, player.hand[inp])
        elif action == "discard":
            game.discard_card_from_hand(player, player.hand[inp])
            return True
    elif inp < 0:
        if action == "play":
            game.phase.next_phase()
        elif action == "discard":
            return False
    else:
        print "Invalid command!"
        
        