import pygame
import sys
from constants import *

class Levels():
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()

    def levels_main(self, WINDOW):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        WINDOW.fill(WHITE)
        pygame.display.update()


