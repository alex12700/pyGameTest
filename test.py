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

hand = []


WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False #exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(str(event.pos) + str((x+width, y+heigth)))

            if event.button == 1 and event.pos <= (x+width, y+heigth) and event.pos >= (x, y):
                test = Card(win, x - 100, y - 100, (0, 0, 255))
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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - heigth - 5:
        y += speed

    # win.fill((0,0,0))

    pygame.draw.rect(win, (0,0,255), (x, y, width, heigth))
    pygame.display.update()

pygame.quit()
