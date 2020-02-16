import pygame

from Cards1 import Card
from Hand import Hand


pygame.init()
sizeWin = (600,500)
win = pygame.display.set_mode(sizeWin)

pygame.display.set_caption("Cubes")

# init of hand and display it
deck = Hand()
hand1 = Hand(deck)


startY = sizeWin[1] - Card.heigth  * Card.padding
stepX  = sizeWin[0]/10
startX = stepX - Card.width/2   # Card.width * (Card.padding - 1)
#Card.width  * Card.padding

for card in hand1.cards:
    card.move(win, startX, startY)
    startX += stepX

run = True
cardSelect = Card((0,0,0), 0)

# add creating of deck and cards in start
# cardTest = Card(win, 100, 100, (0,0,255), 1)

#check area of card for choose
def checkAreaCard(pos, card): #pos = position
    borders = card.getBorders()
    if (pos[0] >= borders[0] and pos[0] <= borders[2]
        and pos[1] >= borders[1] and pos[1] <= borders[3]):
        return True
    else:
        return False

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False #exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # here should be start or restart game or smth else
                print(11)

        # how to check all cards, now check 1 by 1 if
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # choose of card in hand (for if)
                for card in hand1.cards:
                    if checkAreaCard(event.pos, card):
                        # Если выбрана другая карта и предыдущая активна, то выключаем ее
                        if not card.choose and cardSelect.choose:
                            cardSelect.choosen(win)
                        card.choosen(win)
                        cardSelect = card


                pygame.draw.circle(win, (0,255,0), (event.pos), 20) #del
                pygame.display.update() #del
            elif event.button == 3:
                pygame.draw.circle(win, BLUE, event.pos, 20)
                pygame.draw.rect(win, GREEN, (event.pos[0]-10, event.pos[1]-10, 20, 20))
                pygame.display.update()
            elif event.button == 2:
                win.fill(WHITE)
                pygame.display.update()

    pygame.display.update()

pygame.quit()
