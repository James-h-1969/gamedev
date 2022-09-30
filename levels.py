import pygame
import sys
from constants import *

class Levels():
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()

    def levels_main(self, WINDOW, ball, draw, power):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            space_down = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if not ball.in_flight:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_SPACE]:
                    space_down = True
                    if power.strength < 390:
                        power.strength += POWER_BAR_SPEED
                elif space_down == True and not (keys_pressed[pygame.K_SPACE]):
                    space_down = False
                    ball.init_flight_speed = length // 15
                    ball.setup_movement()
                    length = 0
                    ball.in_flight = True
        
        if ball.in_flight:
            if ball.position.y - ball.y_speed <= SCREEN_HEIGHT//2:
                ball.movement()
            else:
                ball.in_flight = False




            ball.angle_line()
            draw.draw_window(WINDOW, ball)




