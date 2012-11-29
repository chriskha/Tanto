import GameObject

class Card(GameObject.GameObject):
    """Tanto Cuore Card class"""
    def __init__(self, cardInfo):
        self.cardNumber = cardInfo['cardNumber']
        self.name = cardInfo['name']
        self.employCost = cardInfo['employCost']
        self.victoryPoints = cardInfo['victoryPoints']
        self.initialQuantity = cardInfo['quantity']
        self.player = None
        