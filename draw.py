import pygame
import os
import math
from constants import *

class Draw():
    def __init__(self):
        self.start_and_end_background = pygame.image.load(os.path.join('img', 'end-background.png')).convert()
        self.logo = pygame.image.load(os.path.join('img', 'scuffed_logo.png')).convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (LOGO_WIDTH, LOGO_HEIGHT))
        self.help_img = pygame.transform.scale(pygame.image.load(os.path.join('img', 'help.jpg')).convert(), (HELP_WIDTH, HELP_HEIGHT))
        self.cross_img = pygame.transform.scale(pygame.image.load(os.path.join('img', 'cross.png')).convert_alpha(), (100, 100))
        self.show_help = False
        
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

    def start_page_background(self, WINDOW, cloud1, cloud2):
        WINDOW.blit(self.start_and_end_background, (0, 0))
        if cloud1.show:
            WINDOW.blit(cloud1.image, (cloud1.x, cloud1.y))
            cloud1.movement()
        if cloud2.show:
            WINDOW.blit(cloud2.image, (cloud2.x, cloud2.y))
            cloud2.movement()

    def draw_start_page_intro(self, WINDOW, text):
        text_display = INTRO_FONT.render(str(text), 1, BLACK)
        WINDOW.blit(text_display, (20, 550))
        pygame.display.update()
 
    
    def draw_start_screen(self, WINDOW, i):
        # START BUTTON #
        x, y = pygame.mouse.get_pos()
        if x > 40 and x < 270 and y > SCREEN_HEIGHT - 120 and y < SCREEN_HEIGHT - 55:
            start_rect = pygame.Rect(20, SCREEN_HEIGHT - 140, 270, 75)    
            border_rect = pygame.Rect(15, SCREEN_HEIGHT - 145, 280 ,85)
            pygame.draw.rect(WINDOW, RED, border_rect)
            pygame.draw.rect(WINDOW, WHITE, start_rect)
            text_placement = (30, SCREEN_HEIGHT - 130)  
            start = START_FONT_LARGE.render("START", 1, BLACK)
            WINDOW.blit(start, text_placement)
        else:
            start_rect = pygame.Rect(40, SCREEN_HEIGHT - 120, 230, 65)    
            border_rect = pygame.Rect(35, SCREEN_HEIGHT - 125, 240 ,75)  
            pygame.draw.rect(WINDOW, RED, border_rect)
            pygame.draw.rect(WINDOW, WHITE, start_rect)
            text_placement = (50, SCREEN_HEIGHT - 110)
            start = START_FONT_SMALL.render("START", 1, BLACK)
            WINDOW.blit(start, text_placement)

        # HELP BUTTON #
        if x > SCREEN_WIDTH - 270 - 40 and x < SCREEN_WIDTH - 40 and y > SCREEN_HEIGHT - 120 and y < SCREEN_HEIGHT - 55:
            help_rect = pygame.Rect(SCREEN_WIDTH - 170 - 60, SCREEN_HEIGHT - 140, 210, 75)    
            border_rect = pygame.Rect(SCREEN_WIDTH - 170 - 65, SCREEN_HEIGHT - 145, 220 ,85)
            pygame.draw.rect(WINDOW, RED, border_rect)
            pygame.draw.rect(WINDOW, WHITE, help_rect)
            text_placement = (SCREEN_WIDTH - 170 - 52, SCREEN_HEIGHT - 130)  
            start = START_FONT_LARGE.render("HELP", 1, BLACK)
            WINDOW.blit(start, text_placement)

        else:
            help_rect = pygame.Rect(SCREEN_WIDTH - 170 - 40, SCREEN_HEIGHT - 120, 170, 65)    
            border_rect = pygame.Rect(SCREEN_WIDTH - 170 - 45, SCREEN_HEIGHT - 125, 180 ,75)
            pygame.draw.rect(WINDOW, RED, border_rect)
            pygame.draw.rect(WINDOW, WHITE, help_rect)
            text_placement = (SCREEN_WIDTH - 170 - 30, SCREEN_HEIGHT - 110)  
            start = START_FONT_SMALL.render("HELP", 1, BLACK)
            WINDOW.blit(start, text_placement)

        # LOGO #
        self.logo = pygame.transform.scale(self.logo, (LOGO_WIDTH*(i/10), LOGO_HEIGHT*(i/10)))
        WINDOW.blit(self.logo, (15, 20))

        if self.show_help:
            WINDOW.blit(self.help_img, (60, 50))
            WINDOW.blit(self.cross_img, (670, 65))

        pygame.display.update()



    def draw_endscreen(self, WINDOW):
        # PLAY AGAIN?
        x, y = pygame.mouse.get_pos()
        if 1: #gonna actually do this
            text_placement = (30, SCREEN_HEIGHT - 130)  
            playagain = PLAYAGAIN_FONT_LARGE.render("PLAY AGAIN", 1, BLACK)
            WINDOW.blit(playagain, text_placement)
        else:
            text_placement = (50, SCREEN_HEIGHT - 110)
            playagain = PLAYAGAIN_FONT_SMALL.render("PLAY AGAIN", 1, BLACK)
            WINDOW.blit(playagain, text_placement)

    def draw_rectangles(WINDOW, walls):
        for rectangle in h_rect_list:
            pygame.draw.rect(WINDOW, DARK_GREEN, rectangle)
            pygame.draw.rect(WINDOW, DARK_GREEN, V_RECT)

