'''
Created on Nov 29, 2012

@author: christopherkha
'''

class PhaseManager(object):
    ''' Handle entering/leaving the game phases '''
    def __init__(self, game, phases, enter_callback, entered_callback, end_callback):
        self.__game = game
        self.__phases = phases
        self.__enterCallback = enter_callback
        self.__enteredCallback = entered_callback
        self.__endCallback = end_callback
        self.__currentPhase = None
        
    def getCurrentPhase(self):
        return self.__currentPhase
    
    def update(self):
        self.__currentPhase.update()
        
    def nextPhase(self):
        ''' Switch to next phase. If the current phase is the last one, go to the first '''
        if self.__currentPhase == None:
            self.__currentPhase = self.__phases[0]
        else:
            self.__endCallback(self.__currentPhase)
            self.__currentPhase.endPhase()
            
            try:
                self.__currentPhase = (self.__phases)[self.__phases.index(self.__currentPhase) + 1]
            except IndexError:
                self.__currentPhase = (self.__phases)[0]
                
        self.__enterCallback(self.__currentPhase)
        self.__currentPhase.enterPhase()
        self.__enteredCallback(self.__currentPhase)
                
class Phase(object):
    '''
    A phase of the game
    '''


    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
        
    def enterPhase(self):
        pass
    
    def update(self):
        pass
    
    def endPhase(self):
        pass
    
class StartingPhase(Phase):
    name = "Starting Phase"
    def enterPhase(self):
        pass
    
    def update(self):
        pass
    
    def endPhase(self):
        pass
    
class ServicePhase(Phase):
    name = "Serving Phase"
    def enterPhase(self):
        pass
    
    def update(self):
        pass
    
    def endPhase(self):
        pass
    
class EmployPhase(Phase):
    name = "Employ Phase"
    def enterPhase(self):
        pass
    
    def update(self):
        pass
    
    def endPhase(self):
        pass
    
class DismissPhase(Phase):
    name = "Dismiss Phase"
    def enterPhase(self):
        pass
    
    def update(self):
        pass
    
    def endPhase(self):
        pass
    
    
        
        