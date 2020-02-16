from random import randint

from Cards1 import Card

suitType = ((0,0,255),(0,255,0),(255,0,0),(255,255,0),(255,0,255))

class Hand():
    cards = []

    def addToHand(self, card):
        self.cards.add(card)

    def __init__(self, deck = None):
        if deck == None:
            self.cards = [Card(suit = j, number = i) for i in range(10) for j in suitType]
        else:
            for _ in range(9):
                self.cards.append(deck.cards.pop(randint(0,len(deck.cards))))
