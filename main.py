import pygame
from constants import *
from start_page import StartPage
from ball import Ball
from levels import Levels
from end_page import *
pygame.font.init()

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    start_page = StartPage()
    level = Levels()
    end_page = EndPage()
    
    start_page.startPage_main(WINDOW) 
    level.levels_main(WINDOW)
    end_page.endPage_main(WINDOW)


    pygame.quit()

if __name__ == "__main__":
    main()