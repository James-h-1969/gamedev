import pygame
import math
from constants import *

class Ball():
    def __init__(self, x, y):
        self.in_flight = False
        self.radius = BALL_RADIUS
        self.position = pygame.Vector2(x, y)
        self.angle_line_vect = pygame.Vector2(1, 1)
        self.initial_flight_speed = 0
        self.direction = 1
        self.anti_grav = False
        self.x_speed = 0
        self.y_speed = 0
        self.shots = 0
        self.hit_vert = False
        self.hit_horizontal = False
        self.Rect = pygame.Rect(0, 0, 0, 0)
        self.current_collision_rect = pygame.Rect(0, 0, 0, 0)

    def angle_line(self):
        if not self.in_flight:
            self.center = pygame.Vector2(self.position.x, self.position.y)
            mouse_pos = pygame.mouse.get_pos()
            delta = mouse_pos - self.center
            self.angle_to_mouse = math.atan2(delta.y, delta.x)
            if mouse_pos[1] <= self.center.y:
                self.angle_line_vect.xy = (40 * math.cos(self.angle_to_mouse), 40 * math.sin(self.angle_to_mouse))
            elif mouse_pos[0] >= self.center.x:
                self.angle_line_vect.xy = (40, 0)
            else:
                self.angle_line_vect.xy = (-40, 0)   
    
    
    def setup_movement(self):
        self.x_speed = self.initial_flight_speed * math.cos(self.angle_to_mouse)
        self.y_speed = abs(self.initial_flight_speed * math.sin(self.angle_to_mouse))
        if self.x_speed > 0:
            self.direction = 1
        else:
            self.direction = -1


    def movement(self):
        if self.hit_horizontal:
            difference_in_y = self.position.y - self.current_collision_rect.center[1]
            if (difference_in_y > 0 and self.y_speed > 0) or (difference_in_y < 0 and self.y_speed < 0):
                self.y_speed = self.y_speed * -1 * BOUNCE_CANCEL 
                self.position.y -= self.y_speed
            else:
                pass
        elif self.position.y < 590 :
            self.position.y -= self.y_speed       
       
        if self.position.x + self.x_speed - 20 < 0 or self.position.x + self.x_speed + 2 * self.radius + 20> SCREEN_WIDTH or self.hit_vert:
            self.x_speed = self.x_speed * -1
            self.direction = self.direction * - 1

        self.position.x += self.x_speed

        if (self.hit_horizontal and self.direction > 0) or (self.position.y >= 590 and self.direction > 0):
            self.x_speed -= FRICTION
        elif (self.hit_horizontal and self.direction < 0) or (self.position.y >= 590 and self.direction < 0):
            self.x_speed += FRICTION
        
        self.y_speed -= 1