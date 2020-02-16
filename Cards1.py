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
    def choosen(self, window):
        xT = self.x - self.width * (self.padding - 1)/2
        yT = self.y - self.heigth * (self.padding - 1)/2
        widthT = self.width * self.padding
        heightT = self.heigth * self.padding

        print(self.choose)

        pygame.draw.rect(window, (0,0,0),
        (xT, yT, widthT, heightT))
        # print(self.choose)

        if not self.choose:
            self.choose = True
            pygame.draw.rect(window, self.suit,
            (xT, yT, widthT, heightT))
            # self.y - self.heigth * (self.padding - 1)/2,
            # self.width * self.padding,
            # self.heigth * self.padding))
        else:
            self.choose = False
            pygame.draw.rect(window, self.suit,
            (self.x,self.y,self.width,self.heigth))



    def addToHand():
        pass

    def move():
        pass
