import pygame
from constants import *
from start_page import StartPage
from ball import Ball
from levels import Levels
pygame.font.init()

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    StartPage.startPage_running() 
    Levels.levels_running()
    





if __name__ == "__main__":
    main()