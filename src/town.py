from src import rules

class Town:
    
    def __init__(self):
        self.general_maids_pile = []
        self.chief_maids_pile = []
        self.private_maids_pile = []
        self.private_maids_up = []
        self.love_cards_pile = []
        self.event_cards_pile = []
        self.town_set = dict()
    
    def create_town(self, card_set):
        rules.create_starting_town(self, card_set)

    def print_all(self):
        for e in self.general_maids_pile:
            print "GM %d of %s" % (len(e), e[0].name)
        for e in self.chief_maids_pile:
            print "CM %d of %s" % (len(e), e[0].name)
        for e in self.private_maids_up:
            print "PM-UP %d of %s" % (len(e), e[0].name)
        for e in self.private_maids_pile:
            print "PM-DN %d of %s" % (len(e), e[0].name)
        for e in self.love_cards_pile:
            print "LV %d of %s" % (len(e), e[0].name)
        for e in self.event_cards_pile:
            print "EV %d of %s" % (len(e), e[0].name)
        
    def print_town(self):
        index = 0
        for i in xrange(len(self.town_set)):
            index = i+1
            s = '%s' % (index)
            quantity = len(self.town_set[s])
            if quantity != 0:
                card = self.town_set[s][0]
                print "%d - %s - %d Love - %d cards left." % (index, card.name, card.employ_cost, quantity)
            else:
                if index <= 12:
                    print "%d - MAID SOLD OUT" % (index)
                elif index > 14 and index <= 17:
                    print "%d - LOVE SOLD OUT" % (index)
                elif index > 17 and index <= 19:
                    print "%d - EVENT SOLD OUT" % (index)
        
        #check private maid pile
        if len(self.private_maids_pile) == 0:
            print "PRIVATE MAIDS PILE EMPTY"
                
        return index
