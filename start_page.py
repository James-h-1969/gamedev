import pygame
import sys
import os
import time
from random import randint
from constants import *
from cloud import Cloud

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
        self.last_time = 0
        self.delta_time = 0

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
                drawing.draw_start_screen(WINDOW, i)
            self.zoom = False
        else:
            drawing.draw_start_screen(WINDOW, 10)
        

    def startPage_main(self, WINDOW, drawing):   
        pygame.mixer.music.load('img/sound.wav')
        pygame.mixer.music.play(-1)
        text = ""
        cloud1 = Cloud(30, randint(20, 50))  
        cloud2 = Cloud(300, randint(50, 70))
        while self.running:
            drawing.start_page_background(WINDOW, cloud1, cloud2)       
            self.clock.tick(FPS)   
            self.delta_time = int(round(time.time() * 1000)) - self.last_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                x, y = pygame.mouse.get_pos()
                if x > 40 and x < 270 and y > SCREEN_HEIGHT - 120 and y < SCREEN_HEIGHT - 55:
                    self.running = False
                    pygame.mixer.music.fadeout(1000)
                if x > SCREEN_WIDTH - 270 - 40 and x < SCREEN_WIDTH - 40 and y > SCREEN_HEIGHT - 120 and y < SCREEN_HEIGHT - 55:
                    drawing.show_help = True
                if drawing.show_help and x > 670 and x < 670 + 100 and y > 65 and y < 65+100:
                    drawing.show_help = False

            ## P1 ##
            if self.p1_running and self.counter == 0:
                drawing.draw_start_page_intro(WINDOW, "")
                pygame.time.delay(DELAY)

            if self.counter < len(self.p1) and self.p1_running:
                text += self.initial_text_main()
                self.counter += 1
                drawing.draw_start_page_intro(WINDOW, text)
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
                drawing.draw_start_page_intro(WINDOW, text)
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
                drawing.draw_start_page_intro(WINDOW, text)
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
                drawing.draw_start_page_intro(WINDOW, text)
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
                drawing.draw_start_page_intro(WINDOW, text)
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
                drawing.draw_start_page_intro(WINDOW, text)
                continue

            elif self.p6_running:
                text = ""
                self.welcome_initial_animation = True
                self.counter = 0
                self.p6_running = False
                pygame.time.delay(DELAY)
                drawing.draw_start_page_intro(WINDOW, text)

            if self.welcome_initial_animation:
                cloud1.show = True
                cloud2.show = True
                self.animation(WINDOW, drawing)







            


            
                

           

                
