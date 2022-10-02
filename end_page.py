import pygame
import sys
import os
from constants import *



class EndPage():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.shots_text = SCORE_FONT.render("6", 1, BLACK)
        self.background = pygame.image.load(os.path.join('img', 'end-background.png'))
        self.scorecard = pygame.image.load(os.path.join('img', 'scorecard.png'))
        self.end_text = INTRO_FONT.render("END OF GAME!", 1, BLACK)

        
    def set_shots(self, shots):
        shots = str(shots)
        self.shots_text = SCORE_FONT.render(shots, 1, BLACK)

    def endPage_main(self, WINDOW):
        while self.running:
            self.clock.tick(FPS)

            #displaying shit
            WINDOW.blit(self.background, (0,0))
            WINDOW.blit(self.scorecard, (190,90))
            WINDOW.blit(self.shots_text, (470, 150))
            WINDOW.blit(self.end_text, (280, 50))
            pygame.display.flip()

            # quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def play_again(self, WINDOW):
        pass


