

class Board: 
  Town town
  Mansion[6] mansions

  def look(self):
    return self.print()

  def print(self):
    print "Board"

  def __init__(self):
    self.town = None
    
