from src.cards import card




""" Maid Types:
    1 = General Maid
    2 = Serving Maid
    3 = Private Maid """
class MaidCard(card.Card):
    maid_title = "Unknown Maid"
    maid_type = 0
    draw = 0
    servings = 0
    love = 0
    employments = 0
    
    def __init__(self, maid_info):
        card.Card.__init__(self, maid_info)
        self.maid_title = maid_info['title']
        #self.maidName = maid_info['name']
        self.maid_type = maid_info['maidCategory']
        self.draw = maid_info['draw']
        self.serving = maid_info['servings']
        self.love = maid_info['love']
        self.employments = maid_info['employments']
        self.is_chambermaid = maid_info['chambermaid']
        self.attachment = []



    def activate(self):
        pass

        