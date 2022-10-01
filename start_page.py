import pygame
import sys
from constants import *

class StartPage():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.counter = 0

    
    def startPage_main(self, WINDOW):
        
        while self.running:
            self.clock.tick(FPS)
            self.counter += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            WINDOW.fill(BLACK)
            pygame.display.update()
            if self.counter > 360:
                self.running = False
                
