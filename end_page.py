import pygame
import sys
import os
from constants import *


# LOAD IMAGES
background = pygame.image.load(os.path.join('img', 'end-background.png'))
background = background.convert()
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class EndPage():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    
    def endPage_main(self, WINDOW):
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            WINDOW.blit(background, (0,0))
            pygame.display.flip()
            pygame.display.update()
                

trial = EndPage()
trial.endPage_main(WINDOW)