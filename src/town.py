from src import rules

class Town:
    
    def __init__(self):
        self.general_maids_pile = []
        self.chief_maids_pile = []
        self.private_maids_pile = []
        self.private_maids_up = []
        self.love_cards_pile = []
        self.event_cards_pile = []
    
    def create_town(self, card_set):
        rules.create_starting_town(self, card_set)

    def print_all(self):
        for e in self.general_maids_pile:
            print "GM %d of %s" % (len(e), e[0].__class__)
        for e in self.chief_maids_pile:
            print "CM %d of %s" % (len(e), e[0].__class__)
        for e in self.private_maids_up:
            print "PM-UP %d of %s" % (len(e), e[0].__class__)
        for e in self.private_maids_pile:
            print "PM-DN %d of %s" % (len(e), e[0].__class__)
        for e in self.love_cards_pile:
            print "LV %d of %s" % (len(e), e[0].__class__)
        for e in self.event_cards_pile:
            print "EV %d of %s" % (len(e), e[0].__class__)
        
