import pygame
import sys
import os
from constants import *

pygame.init()
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# LOAD IMAGES

background = pygame.image.load(os.path.join('img', 'end-background.png'))
WINDOW.blit(background, (0,0))

background = background.convert()
class EndPage():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    
    def endPage_main(self, WINDOW):
        while self.running:
            self.clock.tick(FPS)

            #displaying shit
            pygame.display.flip()

            # quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                

trial = EndPage()
trial.endPage_main(WINDOW)