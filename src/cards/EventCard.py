from src.cards.Card import Card

class EventCard(Card):
    def __init__(self, eventInfo):
        Card.__init__(self, eventInfo)
        

class Illness(EventCard):
    def __init__(self, eventInfo):
        EventCard.__init__(self, eventInfo)
        
    def obtainedEvent(self, game, player):
        pass
    
    def startPhaseEvent(self, game, player):
        pass
        
class BadHabit(EventCard):
    def __init__(self, eventInfo):
        EventCard.__init__(self, eventInfo)

    def obtainedEvent(self, game, player):
        pass
    
    def startPhaseEvent(self, game, player):
        pass
    
    def endGameEvent(self, game, player):
        pass
    
def getEventBuilderFunc(name):
    if name == 'Illness':
        return Illness
    elif name == 'Bad Habit':
        return BadHabit
    else:
        return EventCard