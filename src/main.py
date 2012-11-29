from random import shuffle
import MaidCard
import Love1Card

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

a = []
b = []
def createTown(s):
    for c in a:
        i = 0
        for i in range(c.initialQuantity):
            b.append(c)
            i += 1
    print "Town Created"
    for h in b:
        print h.name

def createDeck(s):
    pass

def buildCardSet(s):
    for m in iter(s):
        if m == 'chiefMaid' or m == 'chamberMaid':
            maid = MaidCard.MaidCard(s[m][0])
            a.append(maid)
        elif m == 'servingMaid':
            for k in range(len(s[m])):
                maid = MaidCard.MaidCard(s[m][k])
                a.append(maid)


def mainloop():
    fp = open("tanto_cuore.json", 'r')
    import json
    s = json.loads(fp.read())
    buildCardSet(s['cardList'])
    for e in range(len(a)):
        print "name: %s\temployCost: %d" % (a[e].name, a[e].employCost)
    createTown(s)
  

mainloop()
