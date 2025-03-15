from turtle import width
import pygame
import pygame.draw
import pygame.key
pygame.init()

win = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Mah first game")

x = [50, 100]
y = [50, 100]
heightR = 20
widthR = 20
velocity = [10, 12]

jumpState = False
jumpCount = 8

run = True
while(run):
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    sprint = pygame.key.get_repeat()

    if keys[pygame.K_UP] and y[0] >= 0:
        y[0] -= velocity[0]
    if keys[pygame.K_DOWN] and y[0] <= 500:
        y[0] += velocity[0]
    if keys[pygame.K_LEFT] and x[0] >= 0:
        x[0] -= velocity[0]
    if keys[pygame.K_RIGHT] and x[0] <= 700:
        x[0] += velocity[0]
    if keys[pygame.K_RETURN]:
        velocity[0] = 30
    else:
        velocity[0] = 10


    if keys[pygame.K_w] and y[1] >= 0:
        y[1] -= velocity[1]
    if keys[pygame.K_s] and y[1] <= 500:
        y[1] += velocity[1]
    if not jumpState:
        if keys[pygame.K_a] and x[1] >= 0:
            x[1] -= velocity[1]
        if keys[pygame.K_d] and x[1] <= 700:
            x[1] += velocity[1]
        if keys[pygame.K_SPACE]:
            jumpState = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y[1] -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            jumpState = False
            jumpCount = 10
        


    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 100), (x[0], y[0], widthR, heightR))
    pygame.draw.rect(win, (100, 0, 100), (x[1], y[1], widthR, heightR))
    pygame.display.update()


pygame.quit


