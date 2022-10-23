import pygame
import random

# initialize  pygame
pygame.init()

# screen creation
screen = pygame.display.set_mode((800, 600))

# infinite loop for game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
