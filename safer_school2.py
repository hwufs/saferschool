# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:09:39 2021

@author: apeng
"""

import os
#import sys
#import random

import pygame
from pygame import mixer
import pygame_widgets
from pygame_widgets.button import Button, ButtonArray

pygame.font.init()

# define colors
WHITE = (255,255,255)
GREEN = (0,192,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREY = (128,128,128)
SILVER = (192,192,192)
PURPLE = (75,0,130)
RED = [200, 50, 0]
DARKRED = [150, 0, 0]


FPS = 60 # frame per second

# define window properties 
WIDTH, HEIGHT = 800, 800 # screen size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SaferSchools")
BIN_FONT = pygame.font.SysFont('comicsans', 50)

global background
global earthquake_icon, fire_icon, bully_icon, internet_icon, gunshooting_icon
global earthquake_icon_x, earthquake_icon_y
global fire_icon_x, fire_icon_y
global bully_icon_x, bully_icon_y
global internet_icon_x, internet_icon_y
global gunshooting_icon_x, gunshooting_icon_y


def load_sprite(folder_name, image_name, xsize, ysize):
    ''' Load and resize a sprite '''
    
    sprite = pygame.image.load(os.path.join(folder_name, image_name))
    sprite = pygame.transform.scale(sprite, (xsize ,ysize))
    return sprite

def load_main_window_sprites():

    global background
    global earthquake_icon, fire_icon, bully_icon, internet_icon, gunshooting_icon    
    global earthquake_icon_x, earthquake_icon_y
    global fire_icon_x, fire_icon_y
    global bully_icon_x, bully_icon_y
    global internet_icon_x, internet_icon_y
    global gunshooting_icon_x, gunshooting_icon_y

 
    background = load_sprite('Assets','school_background.jpg', WIDTH, int(HEIGHT/2))   
    earthquake_icon = load_sprite('Assets','earthquake_icon2.jpg', 110,140)
    fire_icon = load_sprite('Assets','fire.png', 110, 140)
    bully_icon = load_sprite('Assets','bully.png', 110, 140)
    internet_icon = load_sprite('Assets','internet2.jpg', 110,140)
    gunshooting_icon = load_sprite('Assets','gun_shooting.png', 110,140)

    
    earthquake_icon_x = 100
    earthquake_icon_y = 600   
    fire_icon_x = 230
    fire_icon_y = 600
    bully_icon_x = 360
    bully_icon_y = 600     
    internet_icon_x = 490
    internet_icon_y = 600
    gunshooting_icon_x = 620
    gunshooting_icon_y = 600    
    
def load_control_button_sprites():
    
    global prev_question, next_question, return_to_main
    global prev_question_x, prev_question_y
    global next_question_x, next_question_y
    global return_x, return_y
    
    prev_question = load_sprite('Assets','prev_question.png', 50, 50)  
    next_question = load_sprite('Assets', 'next_question.png', 50, 50)
    return_to_main = load_sprite('Assets', 'return_to_main.png', 120, 60)
    
    prev_question_x = 630    
    prev_question_y = 20    
    next_question_x = 700
    next_question_y = 20
    return_x = 630
    return_y = 80

def draw_main_window():
    ''' Draw the main window '''

    # draw the background
    WIN.fill(GREY)
    WIN.blit(background, (0,0))

    # define earthquake, fire, bully, internet, gun shooting icons (surface object)
    
    #draw option icons
    WIN.blit(earthquake_icon, (earthquake_icon_x, earthquake_icon_y))
    WIN.blit(fire_icon, (fire_icon_x, fire_icon_y))
    WIN.blit(bully_icon, (bully_icon_x, bully_icon_y))
    WIN.blit(internet_icon, (internet_icon_x, internet_icon_y))
    WIN.blit(gunshooting_icon, (gunshooting_icon_x, gunshooting_icon_y))

    pygame.display.update()

def draw_control_buttons():
    
    WIN.blit(prev_question, (prev_question_x, prev_question_y))
    WIN.blit(next_question, (next_question_x, next_question_y))
    WIN.blit(return_to_main, (return_x, return_y))
    
def set_main_state():
    global game_state
    game_state = "main"
    
def set_new_question():
    global new_question
    new_question = True
  
def action():
    pass
          
#def draw_control_buttons():
#    
#    # Creates the return button with optional parameters
#    button1 = Button(
#        # Mandatory Parameters
#        WIN,  # Surface to place button on
#        630,  # X-coordinate of top left corner
#        20,  # Y-coordinate of top left corner
#        50,  # Width
#        50,  # Height
#    
#        # Optional Parameters
#        text='<',  # Text to display
#        fontSize=50,  # Size of font
#        margin=20,  # Minimum distance between text/image and edge of button
#        inactiveColour=SILVER,  # Colour of button when not being interacted with
#        hoverColour=GREY,  # Colour of button when being hovered over
#        pressedColour=GREEN,  # Colour of button when being clicked        
#        radius=20,  # Radius of border corners (leave empty for not curved)
#        onClick=lambda: set_main_state()  # Function to call when clicked on
#    )
#    
#    # Creates the 'next' button with optional parameters
#    button2 = Button(
#        # Mandatory Parameters
#        WIN,  # Surface to place button on
#        700,  # X-coordinate of top left corner
#        20,  # Y-coordinate of top left corner
#        50,  # Width
#        50,  # Height
#    
#        # Optional Parameters
#        text='>',  # Text to display
#        fontSize=50,  # Size of font
#        margin=20,  # Minimum distance between text/image and edge of button
#        inactiveColour=SILVER,  # Colour of button when not being interacted with
#        hoverColour=GREY,  # Colour of button when being hovered over
#        pressedColour=GREEN,  # Colour of button when being clicked        
#        radius=20,  # Radius of border corners (leave empty for not curved)
#        onClick=lambda: set_new_question()  # Function to call when clicked on
#    )        
 
def draw_answer_buttons(answer1, answer2, answer3, answer4):
    # create answer buttons
    button_width = 250
    button_height = 80
    button_ori_x = 125
    button_ori_y = 550
    button_step_x = 300
    button_step_y = 100
    
    button_fontsize = 40
    button_margin = 20
    button_radious = 20
    
    button_ans1 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x,  # X-coordinate of top left corner
        button_ori_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters
        text=answer1,  # Text to display
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=RED,  # Colour of button when not being interacted with
        hoverColour=DARKRED,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action()  # Function to call when clicked on
    )

    button_ans2 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x + button_step_x,  # X-coordinate of top left corner
        button_ori_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters
        text=answer2,  # Text to display
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=RED,  # Colour of button when not being interacted with
        hoverColour=DARKRED,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action()  # Function to call when clicked on
    )
    
    button__ans3 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x,  # X-coordinate of top left corner
        button_ori_y + button_step_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters
        text=answer3,  # Text to display
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=RED,  # Colour of button when not being interacted with
        hoverColour=DARKRED,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action()  # Function to call when clicked on
    )

    button__ans4 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x + button_step_x,  # X-coordinate of top left corner
        button_ori_y + button_step_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters
        text=answer4,  # Text to display
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=RED,  # Colour of button when not being interacted with
        hoverColour=DARKRED,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action()  # Function to call when clicked on
    )   


def first_bully_question():
    
    global new_question
    new_question = False # it will change to True when > button is clicked
    
    # draw earthquake background   
    bully_background = load_sprite('Assets', 'bully.gif', WIDTH, int(HEIGHT/2))      
    WIN.fill(SILVER)    
    WIN.blit(bully_background, (0, 0))
   
    question_text = BIN_FONT.render('What will you do?', 1, BLACK)
    WIN.blit(question_text, (100, 450))

    draw_answer_buttons('Tell a Trusted Individual', 'Fight back', 'Ignore Them', '' )
    draw_control_buttons() # draw < (previous) and > (next) buttons

def second_bully_question():
    
    global new_question
    new_question = False # it will change to True when > button is clicked
    
    # draw earthquake background   
    bully_background = load_sprite('Assets', 'bully_question2.jpg', WIDTH, int(HEIGHT/2))      
    WIN.fill(SILVER)    
    WIN.blit(bully_background, (0, 0))
   
    question_text = BIN_FONT.render('Do you recognize this type of bully? ', 1, BLACK)
    WIN.blit(question_text, (100, 450))

    draw_answer_buttons('Physical bully', 'Verbal bully', 'Emotional bully', 'Cyber bully' )
    draw_control_buttons() # draw < (previous) and > (next) buttons
    


#def bully():
#    global game_state
#    game_state = "bully"
#    
#    first_bully_question()        
# 
#    run = True        
#    while run:        
#        
#        if game_state == 'main':
#            run = False
#        else:   
#            if new_question:
#                second_bully_question()
#            else:
##            draw_control_buttons() # draw < (previous) and > (next) buttons
#
#                events = pygame.event.get()       
#                print(events)
#                for event in events:
#                    # need to click a return button
#                    
#                    if event.type == pygame.QUIT:
#                        run = False            
#                        pygame.quit() 
#                print(game_state)            
#                print(game_state == 'main')
#    
#            pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
#            pygame.display.update()
            
            
     
def bully():
    global game_state
    game_state = "bully"
    question_state = 'first question'
    
    first_bully_question()
    
    run = True        
    while run: 
        
        if game_state == 'main':
            run = False
            break
        
        elif question_state == 'first question':
            first_bully_question()    
            
        elif question_state == 'second question':
             second_bully_question()
                      
        events = pygame.event.get()       
        for event in events:
            # need to click a return button
            
            if event.type == pygame.QUIT:
                run = False            
                pygame.quit() 

            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
                    
                    if prev_question.get_rect().collidepoint(mx-prev_question_x, my-prev_question_y):
                        if question_state == 'second question':
                            question_state = 'first question'
                    elif next_question.get_rect().collidepoint(mx-next_question_x, my-next_question_y):
                        if question_state == 'first question':
                            question_state = 'second question'
                    elif return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                        game_state = 'main' 
                                        
            pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
            pygame.display.update()

                        
    return


def earthquake():
    ''' earthquake module '''
    
    global game_state
    game_state = "earthquake"
        
    # draw earthquake background    
    earthquake_background = load_sprite('Assets', 'earthquake_background2.jpg', WIDTH, HEIGHT)
    WIN.fill(SILVER)       
    WIN.blit(earthquake_background, (0, 0))    
    
    # draw control buttons < and >
    draw_control_buttons()

    run = True        
    while run:
        if game_state == 'main':
            run = False
        else:       
            events = pygame.event.get()       
#            print(events)
            for event in events:
                # need to click a return button
                
                if event.type == pygame.QUIT:
                    run = False            
                    pygame.quit() 
                elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                    if event.button == 1:
                        mx, my = event.pos
                        if return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                            game_state = 'main' 
                                        
        pygame.display.update()
    
    return
            
    # earthquake test

def fire():
    global game_state
    game_state = "fire"

    # draw earthquake background        
    fire_background = load_sprite('Assets', 'fire_background.jpg', WIDTH, HEIGHT)   
    WIN.fill(SILVER)      
    WIN.blit(fire_background, (0, 0))

    # draw control buttons < and >    
    draw_control_buttons()
    
    run = True        
    while run:
        if game_state == 'main':
            run = False
        else:       
            events = pygame.event.get()       
            print(events)
            for event in events:
                # need to click a return button
                
                if event.type == pygame.QUIT:
                    run = False            
                    pygame.quit() 
                elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                    if event.button == 1:
                        mx, my = event.pos
                        if return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                            game_state = 'main' 
                            run = False

            pygame.display.update()
    
    return

def internet():
    # draw internet window
    # internet test
    pass

def gun_shooting():
    # draw gun_shooting window
    # gun shooting test
    pass


def main():
    ''' main function of the game '''
    
    load_main_window_sprites()
    load_control_button_sprites()
    
    set_main_state()
    
    clock = pygame.time.Clock()

    run = True
    
    draw_main_window()
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
#                    print(mx, my)
#                    print(earthquake_icon.get_rect())
                    
                    if earthquake_icon.get_rect().collidepoint(mx-earthquake_icon_x, my-earthquake_icon_y):
                        earthquake()
                        draw_main_window()
                        
                    elif fire_icon.get_rect().collidepoint(mx-fire_icon_x, my-fire_icon_y):
                        fire()                       
                        draw_main_window()
                        
                    elif bully_icon.get_rect().collidepoint(mx-bully_icon_x, my-bully_icon_y):
                        bully()
                        draw_main_window()
                        print(run)
                        
                    elif gunshooting_icon.get_rect().collidepoint(mx-gunshooting_icon_x, my-gunshooting_icon_y):
                        gun_shooting()
                        draw_main_window()
                        
                    elif internet_icon.get_rect().collidepoint(mx-internet_icon_x, my-internet_icon_y):
                        internet()
                        draw_main_window()
                    

    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    


