import pygame
from constants import *

class PowerBar():
    def __init__(self):
        self.strength = 0

    def current_power_bar(self):
        self.rect = pygame.Rect(20, 560, self.strength, 20)
        self.bounding_rect = pygame.Rect(15, 555, 400, 30)
        if self.strength < 100:
            self.colour = GREEN
        elif self.strength < 200:
            self.colour = YELLOW
        elif self.strength < 300:
            self.colour = ORANGE
        else:
            self.colour = RED