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

def spaceship():
  screen.blit(spaceshipIMG,(spaceshipX,spaceshipY))

# infinite loop for game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,128,128))
    spaceship()
    pygame.display.update()

