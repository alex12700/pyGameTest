import pygame


class Card():
    choose = False
    #coordinates of card
    x = 0
    y = 0
    number = 0
    suit = (0, 0, 255)
    padding = 1.2 # size to  multiply x2

    heigth = 60
    width = 40

    window = None

    def __init__(self,window, x, y, suit):
        self.x = x
        self.y = y
        self.window = window
        self.suit = suit
        pygame.draw.rect(window, suit,
        (x, y,
        self.width, self.heigth))

    #borders of card
    def getBorders(self):
        return (self.x, self.y, self.x + self.width, self.y + self.heigth)

    #left up border of card
    # def getLUBorder(self):
    #     return (self.x, self.y)

    #scale card if it choose
    def choose(self, window):
        pygame.draw.rect(window, self.suit,
        (self.x - self.width * (self.padding - 1)/2,
        self.y - self.heigth * (self.padding - 1)/2,
        self.width * self.padding,
        self.heigth * self.padding))

    def addToHand():
        pass

    def move():
        pass
