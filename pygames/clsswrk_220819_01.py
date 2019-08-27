# pylint: disable=no-member
import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()

x=50
y=50
width=40
height=60
vol=10


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x=x-vol
    if keys[pygame.K_RIGHT] and x < WIDTH - width:
        x=x+vol
    if keys[pygame.K_UP] and y > 0:
        y=y-vol
    if keys[pygame.K_DOWN] and y < HEIGHT - height:
        y=y+vol


    #without trace
    screen.fill((0,0,0))          
    
    pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
    pygame.display.update()
    clock.tick(60)