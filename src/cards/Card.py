from src import game_object

class Card(game_object.GameObject):
    """Tanto Cuore Card class"""
    def __init__(self, card_info):
        self.card_number = card_info['cardNumber']
        self.name = card_info['cardName']
        self.employ_cost = card_info['employCost']
        self.victory_points = card_info['victoryPoints']
        self.initial_quantity = card_info['quantity']
        self.player = None
        
    def obtained_event(self, game, player):
        pass
    
    def start_phase_event(self, game, player):
        pass
    
    def serve_phase_event(self, game, player):
        pass
    
    def serve_phase_played(self, game, player):
        pass
    
    def employ_phase_event(self, game, player):
        pass
    
    def employ_phase_played(self, game, player):
        pass
    
    def dismiss_phase_event(self, game, player):
        pass
    
    def end_game_event(self, game, player):
        pass
    
    def handler(self, game, player, result):
        pass
    
    def handle_trigger(self, trigger):
        pass