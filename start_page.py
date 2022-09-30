import pygame
import sys
from constants import *

class StartPage():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    
    def startPage_main(self, WINDOW):
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            WINDOW.fill(WHITE)
            pygame.display.update()
                
