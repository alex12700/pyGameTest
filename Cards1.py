import pygame


class Card():
    choose = False
    #coordinates of card
    x = 0
    y = 0
    number = 0
    suit = (0, 0, 255)
    padding = 1.2 # size to  multiply

    heigth = 60
    width = 40

    window = None

    # first init not for hand creation ?delete
    def __init__(self,window, x, y, suit, number):
        self.x = x
        self.y = y
        self.number = number
        self.window = window
        self.suit = suit
        pygame.draw.rect(window, suit,
        (x, y, self.width, self.heigth))

    # WFT? overload doesn't work in python?
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    #borders of card
    def getBorders(self):
        return (self.x, self.y, self.x + self.width, self.y + self.heigth)

    #scale card if it choose
    def choosen(self, window):
        xT = self.x - self.width * (self.padding - 1)/2
        yT = self.y - self.heigth * (self.padding - 1)/2
        widthT = self.width * self.padding
        heightT = self.heigth * self.padding

        pygame.draw.rect(window, (0,0,0),
        (xT, yT, widthT, heightT))

        if not self.choose:
            self.choose = True
            pygame.draw.rect(window, self.suit,
            (xT, yT, widthT, heightT))
        else:
            self.choose = False
            pygame.draw.rect(window, self.suit,
            (self.x,self.y,self.width,self.heigth))

    def move(self, window, x, y):
        xT = self.x - self.width * (self.padding - 1)/2
        yT = self.y - self.heigth * (self.padding - 1)/2
        widthT = self.width * self.padding
        heightT = self.heigth * self.padding

        pygame.draw.rect(window, (0,0,0),
        (xT, yT, widthT, heightT))

        pygame.draw.rect(window, self.suit,
        (x,y,self.width,self.heigth))

    def addToHand(self):
        pass
