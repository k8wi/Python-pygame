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

#Aliens
alienIMG=pygame.image.load('images/Alien.png')
alienX=random.randint(0,800)
alienY=random.randint(0,150)


def spaceship(x,y):
  screen.blit(spaceshipIMG,(x,y))

def aliens(alienX,alienY):
    screen.blit(alienIMG,(alienX,alienY))


# infinite loop for game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Aliens movement



    #Movement Keys pressed
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

    #Spaceship Boundaries
    screen.fill((20,20,20))
    if Xchange>0:
        if spaceshipX<=735.7:
           spaceshipX+=Xchange
    if Xchange<0:
        if spaceshipX>0:
           spaceshipX+=Xchange
    if Ychange>0:
        if spaceshipY <=535.7:
            spaceshipY += Ychange
    if Ychange<0:
        if spaceshipY >350:
            spaceshipY += Ychange

    spaceship(spaceshipX,spaceshipY)
    aliens(alienX,alienY)
    pygame.display.update()

