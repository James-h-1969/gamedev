import pygame
from constants import *
from start_page import StartPage
from ball import Ball
from levels import Levels
from end_page import EndPage
from draw import *
from power_bar import *
pygame.font.init()
pygame.init()

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GOLF HERO")

def main():
    start_page = StartPage()
    level = Levels()
    end_page = EndPage()
    ball = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    drawing = Draw()
    power = PowerBar()
    
    #start_page.startPage_main(WINDOW, drawing) 
    #level.levels_main(WINDOW, ball, drawing, power)
    end_page.set_shots(4)
    end_page.endPage_main(WINDOW)
    

    pygame.quit()

if __name__ == "__main__":
    main()
    trial = EndPage()
    trial.endPage_main(WINDOW)