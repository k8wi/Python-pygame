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
alienIMG=[]
alienX=[]
alienY=[]
lr = []
num_of_aliens=6
for i in range (num_of_aliens):
    alienIMG.append(pygame.image.load('images/Alien.png'))
    alienX.append(random.randint(0,800))
    alienY.append(random.randint(0,150))
    lr.append(random.randint(2,6)/10)
    rand = random.randint(1, 2)
    if rand % 2 == 0:
        lr[i] *= -1

def spaceship(x,y):
  screen.blit(spaceshipIMG,(x,y))

def aliens(alienX,alienY,i):

     screen.blit(alienIMG[i],(alienX,alienY))


# infinite loop for game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Aliens movement
    for i in range (num_of_aliens):
        print(alienY)
        alienX[i] += lr[i]
        if alienX[i]<=0:
            alienY[i] += 15
            lr[i]*=-1

        elif alienX[i]>=736:
            alienY[i] += 15
            lr[i] *=-1


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
    for i in range (num_of_aliens):
      aliens(alienX[i], alienY[i], i)

    pygame.display.update()

