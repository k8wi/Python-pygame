import pygame
import random

# initialize  pygame
pygame.init()

# screen creation
screen = pygame.display.set_mode((800, 600))

#screen title & icon
pygame.display.set_caption("Space Game")
icon=pygame.image.load('images/gameicon.png')
pygame.display.set_icon(icon)

#Spaceship
spaceshipIMG=pygame.image.load('images/spaceship.png')
spaceshipX=370
spaceshipY=480
Xchange=0
Ychange=0

def spaceship(x,y):
  screen.blit(spaceshipIMG,(x,y))

# infinite loop for game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            print("LEFT arrow pressed")
            Xchange=-0.3
        if event.key==pygame.K_RIGHT:
            print("RIGHT arrow pressed")
            Xchange=0.3
        if event.key==pygame.K_UP:
            print("UP arrow pressed")
            Ychange=-0.3
        if event.key==pygame.K_DOWN:
            print("DOWN arrow pressed")
            Ychange=0.3

    if event.type == pygame.KEYUP:
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
            print("Keystroke released")
            Xchange=0
            Ychange=0


    screen.fill((20,20,20))
    spaceshipX+=Xchange
    spaceshipY+=Ychange
    spaceship(spaceshipX,spaceshipY)
    pygame.display.update()

