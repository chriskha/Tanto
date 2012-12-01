from src.cards import card

class EventCard(card.Card):
    def __init__(self, event_info):
        card.Card.__init__(self, event_info)
        

class Illness(EventCard):
    def __init__(self, event_info):
        EventCard.__init__(self, event_info)
        
    def obtained_event(self, game, player):
        pass
    
    def start_phase_event(self, game, player):
        pass
        
class BadHabit(EventCard):
    def __init__(self, event_info):
        EventCard.__init__(self, event_info)

    def obtained_event(self, game, player):
        pass
    
    def start_phase_event(self, game, player):
        pass
    
    def end_game_event(self, game, player):
        pass
    
def get_event_builder_func(name):
    if name == 'Illness':
        return Illness
    elif name == 'Bad Habit':
        return BadHabit
    else:
        return EventCard