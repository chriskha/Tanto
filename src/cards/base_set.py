'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src import phase
from src.cards import maid_card


class Marianne(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)        

class Colette(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_chambered(self, game, player):
        pass
        
class Anise(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Anise ability"
        game.draw_card(player, 3)
        player.employ_count += 1
        
class Ophelia(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Ophelia ability"
        game.draw_card(player, 1)
        player.love_count += 1
        player.service_count += 1
        player.employ_count += 1
        
    def end_game_event(self, game, player):
        # TODO: if more than 1 Ophelia:
        # EVEN, each -2 VP
        # ODD, each 2 VP
        pass

class Sainsbury(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Sainsbury ability"
        
        # TODO: Put 1 Love from hand to town. Take from town 2 Love or maid up to 4 cost to hand
        
class Tenalys(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Tenalys ability"
        player.love_count += 3
        player.employ_count += 1
        
        # TODO: All other players draw card

class Natsumi(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Natsumi ability"
        game.draw_card(player, 1)
        player.service_count += 2
        
        discarded = phase.make_decision(game, player, player.hand, "discard")
        if discarded:
            # TODO: All other players if hand >= 4, discard card
            pass
        

class Nena(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Nena ability"
        player.love_count += 1

class Esquine(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Esquine ability"
        game.draw_card(player, 2)
        
        print "\n%d cards in hand: " % (len(player.hand))
        print player.hand
        print "\nDiscard up to 2 cards?"
        
        for _ in xrange(2):
            discarded = phase.make_decision(game, player, player.hand, "discard")
            
            if discarded:
                player.service_count += 1
            else:
                break
        
class Genevieve(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Genevieve ability"
        game.draw_card(player, 1)
        player.service_count += 1
        player.love_count += 1

class Moine(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Moine ability"
        game.draw_card(player, 2)
        player.employ_count += 2

class Eliza(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)  
        
    def serve_phase_played(self, game, player):
        print "Activate Eliza ability"      
        player.love_count += 2

class Kagari(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Kagari ability"
        player.service_count += 2

class Claire(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Claire ability"
        player.service_count += 1
        
class Safran(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Safran ability"
        player.love_count += 2
        
    def end_game_event(self, game, player):
        # TODO: Chambermaid bonuses for Safran
        # 2 Safran - 4 VP
        # 3 Safran - 8 VP
        # 4 Safran - 12 VP
        pass
    
    def serve_phase_chambered(self, game, player):
        pass
        
class Azure(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Azure ability"
        player.employ_count += 1
        
    def serve_phase_chambered(self, game, player):
        pass

class Viola(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Viola ability" 
        game.draw_card(player, 1)
        
    def serve_phase_chambered(self, game, player):
        pass

class Rouge(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def serve_phase_played(self, game, player):
        print "Activate Rouge ability"
        player.love_count += 1
        
    def serve_phase_chambered(self, game, player):
        pass

class Amber(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
class Nord(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Sora(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Fay(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)        

class Lalande(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Milly(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
class Eugenie(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
class Lucienne(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Rosa(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)        

class Tanya(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
def get_maid_builder_func(name):
    if name == 'Marianne Soleil':
        return Marianne
    elif name == 'Colette Framboise':
        return Colette
    elif name == 'Anise Greenaway':
        return Anise
    elif name == 'Ophelia Grail':
        return Ophelia
    elif name == 'Sainsbury Lockwood':
        return Sainsbury
    elif name == 'Tenalys Trent':
        return Tenalys
    elif name == 'Natsumi Fujikawa':
        return Natsumi
    elif name == 'Nena Wilder':
        return Nena
    elif name == 'Esquine Foret':
        return Esquine
    elif name == 'Genevieve Daubigny':
        return Genevieve
    elif name == 'Moine de Lefevre':
        return Moine
    elif name == 'Eliza Rosewater':
        return Eliza
    elif name == 'Kagari Ichinomiya':
        return Kagari
    elif name == 'Claire Saint-Juste':
        return Claire
    elif name == 'Safran Virginie':
        return Safran
    elif name == 'Azure Crescent':
        return Azure
    elif name == 'Viola Crescent':
        return Viola
    elif name == 'Rouge Crescent':
        return Rouge
    elif name == 'Amber Twilight':
        return Amber
    elif name == 'Nord Twilight':
        return Nord
    elif name == 'Sora Nakachi':
        return Sora
    elif name == 'Fay Longfang':
        return Fay
    elif name == 'Lalande Dreyfus':
        return Lalande
    elif name == 'Milly Violet':
        return Milly
    elif name == 'Eugenie Fontaine':
        return Eugenie
    elif name == 'Lucienne de Marlboro':
        return Lucienne
    elif name == 'Rosa Topaz':
        return Rosa
    elif name == 'Tanya Petrushka':
        return Tanya
    else:
        return maid_card