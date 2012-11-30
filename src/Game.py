'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src.Phase import PhaseManager, StartingPhase, ServicePhase, EmployPhase, \
    DismissPhase
from src.Town import Town
from src.cards.BaseSet import getMaidFuncBuilder
from src.cards.EventCard import getEventBuilderFunc
from src.cards.LoveCard import getLoveBuilderFunc
import json

class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.town = Town()
        self.running = False
        self.phase = PhaseManager(self, 
                                  (StartingPhase(self), ServicePhase(self), EmployPhase(self), DismissPhase(self)),
                                  self.__enteringPhase, self.__enteredPhase, self.__leavingPhase )
        
    def update(self):
        ''' Main game loop '''
        self.phase.update()
    
    def drawCard(self, player, count=1):
        for _ in xrange(count):
            player.drawCard()
        #self.updatePlayer(player)
        
    def __enteringPhase(self, phase):
        ''' Do something special for entering a phase, at the beginning of the phase '''
        pass
    
    def __enteredPhase(self, phase):
        pass
    
    def __leavingPhase(self, phase):
        pass
    
    def setupGame(self, setup, players):
        setList = readJson()
        cardSet = buildCardSet(setList['cardList'])
        self.town.createTown(cardSet)
        
        self.players = players
        players.setupPlayer(self.town)
        
        self.running = True
        self.phase.nextPhase()
        
#move to Util.py ?
def readJson():
    fp = open("tanto_cuore.json", 'r')
    s = json.loads(fp.read())
    return s

def buildCardSet(s):
    a = []
    for m in iter(s):
        if m == 'maid':
            for i in xrange(len(s[m])):
                b = getMaidFuncBuilder(s[m][i]['cardName'])
                #print s[m][i]['cardName']
                if b == None:
                    continue
                maid = b(s[m][i])
                a.append(maid)
        if m == 'love':
            for i in xrange(len(s[m])):
                b = getLoveBuilderFunc(s[m][i]['cardName'])
                #print s[m][i]['cardName']
                if b == None:
                    continue
                loveCard = b(s[m][i])
                a.append(loveCard)
        if m == 'event':
            for i in xrange(len(s[m])):
                b = getEventBuilderFunc(s[m][i]['cardName'])
                #print s[m][i]['cardName']
                if b == None:
                    continue
                eventCard = b(s[m][i])
                a.append(eventCard)
    return a