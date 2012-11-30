'''
Created on Nov 29, 2012

@author: christopherkha
'''
from src.cards.MaidCard import MaidCard
from src.cards.EventCard import EventCard
from src.cards.LoveCard import LoveCard

class Colette(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Marianne(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)        

class Ophelia(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Anise(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
class Sainsbury(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
class Tenalys(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Natsumi(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Nena(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)        

class Esquine(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
    def servePhasePlayed(self, game, player):
        pass
        
class Genevieve(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Moine(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Eliza(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)        

class Kagari(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Claire(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
class Safran(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
class Azure(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Viola(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)        

class Rouge(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Amber(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
class Nord(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Sora(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Fay(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)        

class Lalande(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Milly(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
class Eugenie(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
class Lucienne(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)

class Rosa(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)        

class Tanya(MaidCard):
    def __init__(self, maidInfo):
        MaidCard.__init__(self, maidInfo)
        
def getMaidFuncBuilder(name):
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
        return MaidCard