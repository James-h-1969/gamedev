import pygame
import math
from constants import *

class Draw():
    def __init__(self):
        pass
    def draw_level(self, WINDOW, ball, power, shots):
        #background
        WINDOW.fill(BABY_BLUE)
        
        #ball
        pygame.draw.circle(WINDOW, WHITE, (ball.position.x, ball.position.y), ball.radius)

        #laser
        if not ball.in_flight:
            pygame.draw.line(WINDOW, RED, ball.center, ball.center + ball.angle_line_vect, 3)
        
        #power
        pygame.draw.rect(WINDOW, WHITE, power.bounding_rect)
        pygame.draw.rect(WINDOW, power.colour, power.rect)

        #score
        score = SCORE_FONT.render("Stroke: " + str(shots), 1, BLACK)
        WINDOW.blit(score, (10, 10))


        pygame.display.update()
