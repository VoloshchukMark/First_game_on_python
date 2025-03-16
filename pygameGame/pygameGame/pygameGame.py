from os import walk
from turtle import width
import pygame
import pygame.draw
import pygame.key
pygame.init()

playerWalkRight = [pygame.image.load('sprites\player\R1.png'), pygame.image.load('sprites\player\R2.png'), pygame.image.load('sprites\player\R3.png'), pygame.image.load('sprites\player\R4.png'), pygame.image.load('sprites\player\R5.png'), pygame.image.load('sprites\player\R6.png'), pygame.image.load('sprites\player\R7.png'), pygame.image.load('sprites\player\R8.png'), pygame.image.load('sprites\player\R9.png')]
playerWalkLeft = [pygame.image.load('sprites\player\L1.png'), pygame.image.load('sprites\player\L2.png'), pygame.image.load('sprites\player\L3.png'), pygame.image.load('sprites\player\L4.png'), pygame.image.load('sprites\player\L5.png'), pygame.image.load('sprites\player\L6.png'), pygame.image.load('sprites\player\L7.png'), pygame.image.load('sprites\player\L8.png'), pygame.image.load('sprites\player\L9.png')]
bg = pygame.image.load('sprites/bg/bg.jpg')
player = pygame.image.load('sprites\player\standing.png')


win = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Mah first game")

clock = pygame.time.Clock()

x = 100
y = 430
heightR = 64
widthR = 64
velocity = 5

jumpState = False
jumpCount = 8

side = 0    #0 - left, 1 - right, 2 - idle
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if side == 0:
        win.blit(playerWalkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif side == 1:
        win.blit(playerWalkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(player, (x, y))

    pygame.display.update()


run = True
while(run):
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    sprint = pygame.key.get_repeat()


    if keys[pygame.K_a] and x >= 0:
        x -= velocity
        side = 0
    elif keys[pygame.K_d] and x <= 700:
        x += velocity
        side = 1
    else:
        side = 2
        walkCount = 0
    if keys[pygame.K_RETURN]:
        velocity = 10
    else:
        velocity = 5

    if not jumpState:
        #if keys[pygame.K_w] and y >= 0:
        #    y -= velocity
        #if keys[pygame.K_s] and y <= 500:
        #    y += velocity
        if keys[pygame.K_SPACE]:
            jumpState = True
            side = 2
            walkCount = 0
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
    
    redrawGameWindow()
        


    


pygame.quit


