import pygame
import sys

class StartPage():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    def startPage_main(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()