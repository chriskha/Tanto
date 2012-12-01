from src.cards import card

class LoveCard(card.Card):
    love = 0
    def __init__(self, love_info):
        card.Card.__init__(self, love_info)
        self.love = love_info['love']

    def employ_phase_played(self, game, player):
        self.generate_love(game, player)

    def generate_love(self, game, player):
        player.loveTotal += self.love

class LoveCard1(LoveCard):
    def __init__(self, love_info):
        LoveCard.__init__(self, love_info)
        
class LoveCard2(LoveCard):
    def __init__(self, love_info):
        LoveCard.__init__(self, love_info)
                
class LoveCard3(LoveCard):
    def __init__(self, love_info):
        LoveCard.__init__(self, love_info)
                
def get_love_builder_func(name):
    if name == '1 Love':
        return LoveCard1
    if name == '2 Love':
        return LoveCard2
    if name == '3 Love':
        return LoveCard3