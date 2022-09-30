import pygame
import math
from constants import BALL_RADIUS

class Ball():
    def __init__(self, x, y):
        self.in_flight = False
        self.radius = BALL_RADIUS
        self.position = pygame.Vector2(x, y)
        self.angle_line_vect = pygame.Vector2(1, 1)

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

