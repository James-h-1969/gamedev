import pygame
from constants import *
from start_page import StartPage
from ball import Ball
pygame.font.init()

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    while StartPage.running:
        StartPage.startPage() 






if __name__ == "__main__":
    main()