import math


###SAM'S CODE###
def collision(rect_left, rect_top, width, height,   # rectangle definition
            center_x, center_y, radius):  # circle definition
    rright, rbottom = rect_left + width/2, rect_top + height/2

    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    # reject if boxes do not intersect
    if rright < cleft or rect_left > cright or rbottom < ctop or rect_top > cbottom:
        return False  # no collision possible

    # check whether any point of rectangle is inside circle's radius
    for x in (rect_left, rect_left+width):
        for y in (rect_top, rect_top+height):
            # compare distance between circle's center point and each point of
            # the rectangle with the circle's radius
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True  # collision detected

    # check if center of circle is inside rectangle
    if rect_left <= center_x <= rright and rect_top <= center_y <= rbottom:
        return True  # overlaid

    return False  # no collision detected

def check_for_collision(vel_x, vel_y):
    #checking for collision with vertical wall
    if collision(v_wall[0], v_wall[1], v_wall[2], v_wall[3], Ball.position.x, Ball.position.y, Ball.radius):
        vel_x = -vel_x
        return
    
    i = 0
    while i < len(h_walls):
        if collision(h_walls[i][0], h_walls[i][1], h_walls[i][2], h_walls[i][3], Ball.position.x, Ball.position.y, Ball.radius):
            vel_y = 0 # collision w horizontal wall -> roll
            return
        i+=1
#########


    #enddddd = end_page()
    #enddddd.endPage_main(WINDOW)