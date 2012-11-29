import Card

class Love1Card(Card.Card):
  def __init__(self):
    #super()
    self.love = 1

  def activate(self):
    self.generateLove()

  def generateLove(self):
    self.player.loveTotal += self.love
