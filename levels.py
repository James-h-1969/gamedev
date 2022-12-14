import pygame
import sys
from constants import *
import math
from walls import Walls

class Levels():
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.space_down = False
        self.shots = 0
        self.jump_off = False

    def levels_main(self, WINDOW, ball, drawing, power):
        pygame.mixer.music.load('img/legit 3 head.wav')
        pygame.mixer.music.play(-1)
        self.running = True
        walls = Walls()
        walls.initialise_walls()
        while self.running:
            self.clock.tick(FPS)
            ball.rect = pygame.Rect(ball.position.x, ball.position.y, ball.radius * 2, ball.radius * 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            hole_y = 578
            hole_x = 400
            in_the_hole = (hole_x <= ball.position.x <= (hole_x + 20)) and (hole_y <= (ball.position.y + 5) <= (hole_y + 20))
            if in_the_hole:
                self.running = False

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
                    self.jump_off = True



            if ball.in_flight:
                if ball.position.x > 350 and ball.position.x < 450 and ball.position.y < 150 and ball.position.y > 120:
                    ball.position.x = ball.old_x
                    ball.position.y = ball.old_y
                    self.shots += 1
                    ball.in_flight = False
                else:            
                    if (ball.direction > 0 and ball.x_speed > 0) or (ball.direction < 0 and ball.x_speed < 0) or self.hit_vert:
                        if self.jump_off:
                            self.hit_vert = False
                            self.hit_horizontal = False
                            self.jump_off = False
                            ball.position.y -= 10
                        else:
                            walls.check_collisions(ball)
                        if ball.position.y > 590:
                            ball.position.y = 590
                        ball.movement()
                    else:
                        ball.in_flight = False

            power.current_power_bar()

            ball.angle_line()
            drawing.draw_level(WINDOW, ball, power, self.shots, walls)






