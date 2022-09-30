import pygame
from constants import *
from start_page import StartPage
from ball import Ball
from levels import Levels
pygame.font.init()

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    start_page = StartPage()
    levels = Levels()
    
    start_page.startPage_main(WINDOW) 
    levels.levels_main(WINDOW)
    pygame.quit()

if __name__ == "__main__":
    main()