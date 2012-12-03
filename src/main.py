from src import game
from src import player


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

game = game.Game()
players = player.Player(game)

def mainloop():
    game.setup_game(None, players)
    
    while game.running:
        game.update()
  

mainloop()
