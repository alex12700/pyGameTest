import pygame

from Cards1 import Card


pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Cubes")

x = 250
y = 350
width = 40
heigth = 60
speed = 5
run = True


WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

# add creating of deck and cards in start
cardTest = Card(win,100,100,(0,0,255))

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
            if event.button == 1 and checkAreaCard(event.pos, cardTest):
                cardTest.choosen(win)
                # test = Card(win, 150, 150, (255, 255, 255))

                pygame.draw.circle(win, RED, (event.pos), 20)
                pygame.display.update()
                print(1)
            elif event.button == 3:
                pygame.draw.circle(win, BLUE, event.pos, 20)
                pygame.draw.rect(win, GREEN, (event.pos[0]-10, event.pos[1]-10, 20, 20))
                pygame.display.update()
            elif event.button == 2:
                win.fill(WHITE)
                pygame.display.update()

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT] and x > 5:
    #     x -= speed
    # if keys[pygame.K_RIGHT] and x < 500 - width - 5:
    #     x += speed
    # if keys[pygame.K_UP] and y > 5:
    #     y -= speed
    # if keys[pygame.K_DOWN] and y < 500 - heigth - 5:
    #     y += speed

    # win.fill((0,0,0))

    # pygame.draw.rect(win, (0,0,255), (x, y, width, heigth))

    pygame.display.update()

pygame.quit()
