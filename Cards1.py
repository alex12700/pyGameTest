import pygame


class Card():
    choose = False
    # coordinates = [0, 0]
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

    def getArea():
        return self.x

    def choose(window):
        pygame.draw.rect(window, self.suit,
        (self.x * self.padding, self.y * self.padding,
        self.width * self.padding, self.heigth * self.padding))

    def addToHand():
        pass

    def move():
        pass
