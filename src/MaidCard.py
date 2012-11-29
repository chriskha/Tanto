

""" Maid Types:
    1 = General Maid
    2 = Serving Maid
    3 = Private Maid """

import Card

class MaidCard(Card.Card):
    def __init__(self, maidInfo):
        Card.Card.__init__(self, maidInfo)
        self.maidTitle = ""
        #self.maidName = maidInfo['name']
        self.maidType = 0
        self.calling = 0
        self.serving = 0
        self.love = 0
        self.employing = 0
        self.isChambermaid = False
        self.attachment = []



    def activate(self):
        self.generateCalling()
        self.generateServing()
        self.generateLove()
        self.generateEmploying()
        self.doEffect()

  
