import pygame
import sys
from constants import *
import math

class Levels():
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.space_down = False
        self.shots = 0

    def levels_main(self, WINDOW, ball, draw, power):
        self.running = True

        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if not ball.in_flight:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_SPACE]:
                    self.space_down = True
                    if power.strength < MAX_POWER:
                        power.strength += POWER_BAR_SPEED
                elif self.space_down == True and not (keys_pressed[pygame.K_SPACE]):
                    self.space_down = False
                    ball.initial_flight_speed = power.strength // 15
                    ball.setup_movement()
                    power.strength = 0
                    self.shots += 1
                    ball.in_flight = True
            if ball.in_flight:
                if (ball.direction > 0 and ball.x_speed > 0) or (ball.direction < 0 and ball.x_speed < 0):
                    ball.movement()
                else:
                    ball.in_flight = False

            power.current_power_bar()

            ball.angle_line()
            draw.draw_level(WINDOW, ball, power, self.shots)





