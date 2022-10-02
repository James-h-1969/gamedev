import pygame 


import pygame
from constants import*

class Walls():
    def __init__(self):
        self.h_rect_list = []


    def initialise_walls(self):
        H_RECT_1 = pygame.Rect(0, 450, H_RECT_WIDTH, H_RECT_HEIGHT)
        H_RECT_2 = pygame.Rect(SCREEN_WIDTH/2 - V_RECT_WIDTH - H_RECT_WIDTH , 300, H_RECT_WIDTH, H_RECT_HEIGHT)
        H_RECT_3 = pygame.Rect(0, 170, H_RECT_WIDTH, H_RECT_HEIGHT)
        H_RECT_4 = pygame.Rect(SCREEN_WIDTH/2, 200, H_RECT_WIDTH, H_RECT_HEIGHT)
        H_RECT_5 = pygame.Rect(SCREEN_WIDTH - H_RECT_WIDTH, 350, H_RECT_WIDTH, H_RECT_HEIGHT)
        #List of horizontal rectangles
        self.h_rect_list = [H_RECT_1, H_RECT_2, H_RECT_3, H_RECT_4, H_RECT_5]
        #Vertical wall list
        self.v_rect = [pygame.Rect(SCREEN_WIDTH/2 - V_RECT_WIDTH, 150, V_RECT_WIDTH, V_RECT_HEIGHT)]


    def check_collisions(self, ball):
        if (ball.rect).collidelist(self.h_rect_list) >= 0:
            ball.hit_horizontal = True
            print("JUST COLLIDED!!!!")
        else:
            ball.hit_horizontal = False
       
        if (ball.rect).collidelist(self.v_rect) >= 0:
            ball.hit_vert = True
            print("JUST COLLIDED!!!!")
        else:
            ball.hit_vert = False
            

    # def collision(rect_left, rect_top, width, height,   # rectangle definition
    #           center_x, center_y, radius):  # circle definition
    #     rright, rbottom = rect_left + width/2, rect_top + height/2

    #     cleft, ctop     = center_x-radius, center_y-radius
    #     cright, cbottom = center_x+radius, center_y+radius

    #     # reject if boxes do not intersect
    #     if rright < cleft or rect_left > cright or rbottom < ctop or rect_top > cbottom:
    #         return False  # no collision possible

    #     # check whether any point of rectangle is inside circle's radius
    #     for x in (rect_left, rect_left+width):
    #         for y in (rect_top, rect_top+height):
    #             # compare distance between circle's center point and each point of
    #             # the rectangle with the circle's radius
    #             if math.hypot(x-center_x, y-center_y) <= radius:
    #                 return True  # collision detected

    #     # check if center of circle is inside rectangle
    #     if rect_left <= center_x <= rright and rect_top <= center_y <= rbottom:
    #         return True  # overlaid

    #     return False  # no collision detected

    # def check_for_collision(vel_x, vel_y):
    #     #checking for collision with vertical wall
    #     if collision(v_wall[0], v_wall[1], v_wall[2], v_wall[3], Ball.position.x, Ball.position.y, Ball.radius):
    #         vel_x = -vel_x
    #         return
        
    #     #collision w horizontal wall -> roll
    #     i = 0
    #     while i < len(h_walls):
    #         if collision(h_walls[i][0], h_walls[i][1], h_walls[i][2], h_walls[i][3], Ball.position.x, Ball.position.y, Ball.radius):
    #             vel_y = 0 
    #             return
    #         i+=1
#########