import GameObject

class Card(GameObject.GameObject):
    """Tanto Cuore Card class"""
    def __init__(self, cardInfo):
        self.cardNumber = cardInfo['cardNumber']
        self.name = cardInfo['cardName']
        self.employCost = cardInfo['employCost']
        self.victoryPoints = cardInfo['victoryPoints']
        self.initialQuantity = cardInfo['quantity']
        self.player = None
        
    def obtainedEvent(self, game, player):
        pass
    
    def startPhaseEvent(self, game, player):
        pass
    
    def servePhaseEvent(self, game, player):
        pass
    
    def servePhasePlayed(self, game, player):
        pass
    
    def employPhaseEvent(self, game, player):
        pass
    
    def employPhasePlayed(self, game, player):
        pass
    
    def dismissPhaseEvent(self, game, player):
        pass
    
    def endGameEvent(self, game, player):
        pass
    
    def handler(self, game, player, result):
        pass
    
    def handle_trigger(self, trigger):
        pass