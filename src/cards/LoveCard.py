from src.cards.Card import Card

class LoveCard(Card):
    love = 0
    def __init__(self, loveInfo):
        Card.__init__(self, loveInfo)
        self.love = loveInfo['love']

    def employPhasePlayed(self, game, player):
        self.generateLove(game, player)

    def generateLove(self, game, player):
        player.loveTotal += self.love

class LoveCard1(LoveCard):
    def __init__(self, loveInfo):
        LoveCard.__init__(self, loveInfo)
        
class LoveCard2(LoveCard):
    def __init__(self, loveInfo):
        LoveCard.__init__(self, loveInfo)
                
class LoveCard3(LoveCard):
    def __init__(self, loveInfo):
        LoveCard.__init__(self, loveInfo)
                
def getLoveBuilderFunc(name):
    if name == '1 Love':
        return LoveCard1
    if name == '2 Love':
        return LoveCard2
    if name == '3 Love':
        return LoveCard3