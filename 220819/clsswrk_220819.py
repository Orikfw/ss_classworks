import pygame
# pylint: disable=no-member
ORANGE = (255, 150, 100)
game__display = pygame.display.set_mode((600,600))
pygame.display.set_caption('HI')
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    game__display.fill((0,0,0))
    pygame.draw.line(game__display, (192,192,192), [5,5], [500,500],5)
    pygame.draw.rect(game__display, (150,150,200), [50,100,200,600])
    pygame.draw.polygon(game__display, (200,150,20), [[250, 110], [280, 150], [190, 190], [130, 130]])
    pygame.draw.aalines(game__display, (200,150,20), True, [[250, 110], [280, 150], [190, 190], [130, 130]])
    pygame.draw.circle(game__display, (192,192,192), [200,200], 100, 7)
    pygame.draw.ellipse(game__display, (200,200,100), (10,50,250,100))
    pygame.draw.arc(game__display, (255,255,255), (10, 50, 280, 100), 0, 3.14)
    pygame.draw.arc(game__display, (75,20,35), (50, 30, 200, 150), 3.14, 2*3.14, 3)
    pygame.display.update()
    clock.tick(30)