'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src.cards import maid_card

class Colette(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Marianne(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)        

class Ophelia(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Anise(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
class Sainsbury(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
class Tenalys(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Natsumi(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Nena(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)        

class Esquine(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
    def servePhasePlayed(self, game, player):
        pass
        
class Genevieve(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Moine(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Eliza(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)        

class Kagari(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Claire(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
class Safran(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)
        
class Azure(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

class Viola(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)        

class Rouge(maid_card.MaidCard):
    def __init__(self, maid_info):
        maid_card.MaidCard.__init__(self, maid_info)

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