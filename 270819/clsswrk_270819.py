import pygame
import random as rd
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SIZE = WIN_HEIGHT, WIN_WIDTH = (800, 600)
COUNT_SHAPES = 1000


class Rectangle():
    def __init__(self, x=0, y=0, height=0, width=0, change_x=0, change_y=0, color=None):
        self.x = rd.randint(0, 730)
        self.y = rd.randint(0, 530)
        self.height = rd.randint(20, 70)
        self.width = rd.randint(20, 70)
        self.change_x = rd.randint(-3, 3)
        self.change_y = rd.randint(-3, 3)
        self.color = (rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.height, self.width])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y


class Ellipse(Rectangle):
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.height, self.width])

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('My Game')

done = False
my_list = []

for i in range(COUNT_SHAPES):
    my_obj = Rectangle()
    my_list.append(my_obj)
for i in range(COUNT_SHAPES):
    my_obj = Ellipse()
    my_list.append(my_obj)
rd.shuffle(my_list)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for my_obj in my_list:
        my_obj.draw(screen)

    pygame.display.flip()

pygame.quit()
