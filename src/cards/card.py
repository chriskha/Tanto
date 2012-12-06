from src import game_object
import copy

class Card(game_object.GameObject):
    """Tanto Cuore Card class"""
    def __init__(self, card_info):
        self.card_number = card_info['cardNumber']
        self.name = card_info['cardName']
        self.employ_cost = card_info['employCost']
        self.victory_points = card_info['victoryPoints']
        self.initial_quantity = card_info['quantity']
        self.player = None
        
    def copy(self):
        copied_card = copy.copy(self)
        copied_card.card_number = self.card_number
        copied_card.name = self.name
        copied_card.employ_cost = self.employ_cost
        copied_card.victory_points = self.victory_points
        copied_card.initial_quantity = self.initial_quantity
        copied_card.player = self.player
        
        return copied_card
        
    def obtained_event(self, game, player):
        pass
    
    def start_phase_event(self, game, player):
        pass
    
    def serve_phase_event(self, game, player):
        pass
    
    def serve_phase_played(self, game, player):
        pass
    
    def serve_phase_chambered(self, game, player):
        pass
    
    def employ_phase_event(self, game, player):
        pass
    
    def employ_phase_played(self, game, player):
        pass
    
    def dismiss_phase_event(self, game, player):
        pass
    
    def end_game_event(self, game, player):
        pass
    
    def activate(self, game, player):
        pass
    
    def handler(self, game, player, result):
        pass
    
    def handle_trigger(self, trigger):
        pass