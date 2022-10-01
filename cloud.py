import pygame
from random import randint
import os
from constants import *

class Cloud():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = randint(-1, 1)
        self.show = False
        if self.direction >= 0:
            self.x_speed = CLOUD_SPEED
        else:
            self.x_speed = -1 * CLOUD_SPEED
        self.image = pygame.image.load(os.path.join('img', 'cloud.png')).convert_alpha()
        self.width = 300 * randint(5, 10)/10
        self.height = 200 * randint(5, 10)/10
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def movement(self):
        if self.x + self.x_speed + self.width >= SCREEN_WIDTH or self.x + self.x_speed <= 0:
            self.x_speed = self.x_speed * -1
        self.x += self.x_speed