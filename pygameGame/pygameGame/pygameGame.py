from os import walk
from turtle import width
import pygame
import pygame.draw
import pygame.key
pygame.init()

win = pygame.display.set_mode((700, 480))
pygame.display.set_caption("Mah first game")
clock = pygame.time.Clock()

playerWalkRight = [pygame.image.load('sprites\player\R1.png'), pygame.image.load('sprites\player\R2.png'), pygame.image.load('sprites\player\R3.png'), pygame.image.load('sprites\player\R4.png'), pygame.image.load('sprites\player\R5.png'), pygame.image.load('sprites\player\R6.png'), pygame.image.load('sprites\player\R7.png'), pygame.image.load('sprites\player\R8.png'), pygame.image.load('sprites\player\R9.png')]
playerWalkLeft = [pygame.image.load('sprites\player\L1.png'), pygame.image.load('sprites\player\L2.png'), pygame.image.load('sprites\player\L3.png'), pygame.image.load('sprites\player\L4.png'), pygame.image.load('sprites\player\L5.png'), pygame.image.load('sprites\player\L6.png'), pygame.image.load('sprites\player\L7.png'), pygame.image.load('sprites\player\L8.png'), pygame.image.load('sprites\player\L9.png')]
bg = pygame.image.load('sprites/bg/bg.jpg')
playerIdle = pygame.image.load('sprites\player\standing.png')

class player(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.velocity = 5
        self.jumpState = False
        self.jumpCount = 8
        self.side = 2           #0 - left, 1 - right, 2 - idle
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.side == 0:
            win.blit(playerWalkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif player1.side == 1:
            win.blit(playerWalkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(playerIdle, (self.x, self.y))


def redrawGameWindow():
    win.blit(bg, (0,0))

    player1.draw(win)
    

    pygame.display.update()


run = True
player1 = player(100, 400, 64, 64)
while(run):
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    sprint = pygame.key.get_repeat()


    if keys[pygame.K_a] and player1.x >= 0:
        player1.x -= player1.velocity
        player1.side = 0
    elif keys[pygame.K_d] and player1.x <= 700:
        player1.x += player1.velocity
        player1.side = 1
    else:
        player1.side = 2
        player1.walkCount = 0
    if keys[pygame.K_RETURN]:
        player1.velocity = 10
    else:
        player1.velocity = 5

    if not player1.jumpState:
        #if keys[pygame.K_w] and y >= 0:
        #    y -= velocity
        #if keys[pygame.K_s] and y <= 500:
        #    y += velocity
        if keys[pygame.K_SPACE]:
            player1.jumpState = True
            player1.side = 2
            player1.walkCount = 0
    else:
        if player1.jumpCount >= -8:
            neg = 1
            if player1.jumpCount < 0:
                neg = -1
            player1.y -= (player1.jumpCount ** 2) / 2 * neg
            player1.jumpCount -= 1
        else:
            player1.jumpState = False
            player1.jumpCount = 8
    
    redrawGameWindow()
        


    


pygame.quit


