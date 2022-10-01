import pygame
import sys
import os
from constants import *


class StartPage():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.initial_text = False
        self.p1_running = True
        self.p2_running = False
        self.p3_running = False
        self.p4_running = False
        self.p5_running = False
        self.p6_running = False
        self.p1 = "A long, long time ago ..."
        self.p2 = "On a golf course far, far away ..."
        self.p3 = "A young golf ball was madly in love with its golfer..."
        self.p4 = "Until one day the golfer used another ball :("
        self.p5 = "The ULTIMATE heartbreak..."
        self.p6 = "Introducing ..."
        self.welcome_initial_animation = False
        self.zoom = True
        self.ready_to_start = False

    def initial_text_main(self):
        if self.p1_running:
            text = self.p1[self.counter]
            return text
        if self.p2_running:
            text = self.p2[self.counter]
            return text
        if self.p3_running:
            text = self.p3[self.counter]
            return text
        if self.p4_running:
            text = self.p4[self.counter]
            return text
        if self.p5_running:
            text = self.p5[self.counter]
            return text
        if self.p6_running:
            text = self.p6[self.counter]
            return text
        else: return ""

    def animation(self, WINDOW, drawing):
        if self.zoom:
            for i in range(1, 11):
                drawing.draw_start_screen(WINDOW, i, self)
            self.zoom = False
        else:
            drawing.draw_start_screen(WINDOW, 10, self)
        

    def startPage_main(self, WINDOW, drawing):   
        text = ""
        while self.running:            
            self.clock.tick(FPS)   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                x, y = pygame.mouse.get_pos()
                if x > 40 and x < 270 and y > SCREEN_HEIGHT - 120 and y < SCREEN_HEIGHT - 55:
                    self.running = False


            
            ## P1 ##
            if self.p1_running and self.counter == 0:
                drawing.draw_start_page_intro(WINDOW, "", 250)
                pygame.time.delay(DELAY)
            if self.counter < len(self.p1) and self.p1_running:
                text += self.initial_text_main()
                self.counter += 1
                drawing.draw_start_page_intro(WINDOW, text, 250)
                continue

            elif self.p1_running:
                text = ""
                self.p2_running = True
                self.counter = 0
                self.p1_running = False
                pygame.time.delay(DELAY)

            ## P2 ##
            if self.counter < len(self.p2) and self.p2_running:
                text += self.initial_text_main()
                self.counter += 1
                drawing.draw_start_page_intro(WINDOW, text, 150)
                continue

            elif self.p2_running:
                text = ""
                self.p3_running = True
                self.counter = 0
                self.p2_running = False
                pygame.time.delay(DELAY)

            ## P3 ##
            if self.counter < len(self.p3) and self.p3_running:
                text += self.initial_text_main()
                self.counter += 1
                drawing.draw_start_page_intro(WINDOW, text, 50)
                continue

            elif self.p3_running:
                text = ""
                self.p4_running = True
                self.counter = 0
                self.p3_running = False
                pygame.time.delay(DELAY)

            ## P4 ##
            if self.counter < len(self.p4) and self.p4_running:
                text += self.initial_text_main()
                self.counter += 1
                drawing.draw_start_page_intro(WINDOW, text, 10)
                continue

            elif self.p4_running:
                text = ""
                self.p5_running = True
                self.counter = 0
                self.p4_running = False
                pygame.time.delay(DELAY)

            ## P5 ##
            if self.counter < len(self.p5) and self.p5_running:
                text += self.initial_text_main()
                self.counter += 1
                drawing.draw_start_page_intro(WINDOW, text, 170)
                continue
            
            elif self.p5_running:
                text = ""
                self.p6_running = True
                self.counter = 0
                self.p5_running = False
                pygame.time.delay(DELAY)

            ## P6 ##
            if self.counter < len(self.p6) and self.p6_running:
                text += self.initial_text_main()
                self.counter += 1
                drawing.draw_start_page_intro(WINDOW, text, 200)
                continue

            elif self.p6_running:
                text = ""
                self.welcome_initial_animation = True
                self.counter = 0
                self.p6_running = False
                pygame.time.delay(DELAY)
                drawing.draw_start_page_intro(WINDOW, text, 200)

            if self.welcome_initial_animation:
                self.animation(WINDOW, drawing)





            


            
                

           

                
