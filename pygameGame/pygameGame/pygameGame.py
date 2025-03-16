from turtle import width
import pygame
import pygame.draw
import pygame.key
pygame.init()

win = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Mah first game")

x = 100
y = 100
heightR = 20
widthR = 20
velocity = 8

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


    if keys[pygame.K_a] and x >= 0:
        x -= velocity
    if keys[pygame.K_d] and x <= 700:
        x += velocity
    if keys[pygame.K_RETURN]:
        velocity = 16
    else:
        velocity = 8

    if not jumpState:
        if keys[pygame.K_w] and y >= 0:
            y -= velocity
        if keys[pygame.K_s] and y <= 500:
            y += velocity
        if keys[pygame.K_SPACE]:
            jumpState = True
    else:
        if jumpCount >= -8:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            jumpState = False
            jumpCount = 8
        


    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 100), (x, y, widthR, heightR))
    pygame.display.update()


pygame.quit


