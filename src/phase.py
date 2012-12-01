'''
Created on Nov 29, 2012

@author: christopherkha
'''

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
    def enter_phase(self):
        pass
    
    def update(self):
        pass
    
    def end_phase(self):
        pass
    
class ServicePhase(Phase):
    name = "Serving Phase"
    def enter_phase(self):
        pass
    
    def update(self):
        pass
    
    def end_phase(self):
        pass
    
class EmployPhase(Phase):
    name = "Employ Phase"
    def enter_phase(self):
        pass
    
    def update(self):
        pass
    
    def end_phase(self):
        pass
    
class DismissPhase(Phase):
    name = "Dismiss Phase"
    def enter_phase(self):
        pass
    
    def update(self):
        pass
    
    def end_phase(self):
        pass
    
    
        
        