

""" Maid Types:
    1 = General Maid
    2 = Serving Maid
    3 = Private Maid """

from src.cards.Card import Card
class MaidCard(Card):
    maidTitle = "Unknown Maid"
    maidType = 0
    draw = 0
    servings = 0
    love = 0
    employments = 0
    
    def __init__(self, maidInfo):
        Card.__init__(self, maidInfo)
        self.maidTitle = maidInfo['title']
        #self.maidName = maidInfo['name']
        self.maidType = maidInfo['maidCategory']
        self.draw = maidInfo['draw']
        self.serving = maidInfo['servings']
        self.love = maidInfo['love']
        self.employments = maidInfo['employments']
        self.isChambermaid = maidInfo['chambermaid']
        self.attachment = []



    def activate(self):
        self.generateCalling()
        self.generateServing()
        self.generateLove()
        self.generateEmploying()
        self.doEffect()

        