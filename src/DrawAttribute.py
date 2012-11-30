'''
Created on Nov 28, 2012

@author: christopherkha
'''

import CardAttribute

class DrawAttribute(CardAttribute.CardAttribute):
    '''
    classdocs
    '''
    numDraw = 0

    def __init__(self, n):
        '''
        Constructor
        '''
        self.numDraw = n
        
        
    def activate(self):
        #player.draw(self.numDraw)
        pass