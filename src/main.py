from random import shuffle
from src.Game import Game
from src.Player import Player
from src.Town import Town
from src.cards.BaseSet import getMaidFuncBuilder
from src.cards.EventCard import getEventBuilderFunc
from src.cards.LoveCard import getLoveBuilderFunc
from src.cards.MaidCard import MaidCard


"""global cardUID


def mainloop():
  cardUID = 0
  deck = []
  love1card = Love1Card.Love1Card()
  for i in range(7):
    deck.append((love1card,cardUID))
    cardUID += 1
  colette = Card.Card()
  for i in range(3):
    deck.append((colette,cardUID))
    cardUID += 1

  shuffle(deck)
  print "Game START"
  print deck"""

game = Game()
players = Player(game)

def mainloop():
    Game.setupGame(game, None, players)
  

mainloop()
