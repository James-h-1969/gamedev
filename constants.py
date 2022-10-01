import pygame
import os
pygame.font.init()

###SCREEN###
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
FPS = 60


###BALL###
BALL_RADIUS = 5
FRICTION = 0.4
BOUNCE_CANCEL = 0.35


###POWER_BAR###
POWER_BAR_SPEED = 5
MAX_POWER = 390
PADDING = 20


###COLOURS###
WHITE = (255, 255, 255)
BLUE = (137, 207, 240)
BABY_BLUE = (172, 217, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

### SCORE ###
SCORE_FONT = pygame.font.SysFont('Arial', 20)
INTRO_FONT = pygame.font.Font('img/fonts/Minecraft.ttf', 30)
START_FONT_SMALL = pygame.font.Font('img/fonts/Minecraft.ttf', 60)
START_FONT_LARGE = pygame.font.Font('img/fonts/Minecraft.ttf', 75)

## ANIMATION ##
ANIMATION_SPEED = 0.2
DELAY = 1000

## LOGO ##
LOGO_HEIGHT = 480
LOGO_WIDTH = 1000

## CLOUD ##
CLOUD_SPEED = 2

## HELP ##
HELP_WIDTH = 700
HELP_HEIGHT = 400

## PLAY AGAIN
PLAYAGAIN_FONT_SMALL = pygame.font.Font('img/fonts/Minecraft.ttf', 30)
PLAYAGAIN_FONT_LARGE = pygame.font.Font('img/fonts/Minecraft.ttf', 40)