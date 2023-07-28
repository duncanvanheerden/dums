import pygame as pg
import sys
import os
from main.interface.Button import Button as button

fps = 60

class Interface():

    def __init__(self):
        pg.init()

    def window(self):
        # Set the dimensions of the window
        width = 0
        height = 0
        
        # Get current working directory
        cwd = os.getcwd()

        # Create the window display
        # screen = pg.display.set_mode((width, height))
        
        #Create a Full screen
        screen = pg.display.set_mode((0,0),pg.FULLSCREEN)

        # Set the title of the window
        pg.display.set_caption("My Pygame Window")
        
        #load button images
        start_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/start_button.png'))
        rules_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/rules.png'))
        singlePlay_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/Single_player.png'))
        multiplay_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/Multiplayer.png'))
        homescreen_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/home_screen.png'))
        playerVplayer_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/1v1_button.png'))
        playerVplayerVplayer_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/1v1_button.png'))
        player2Vplayer2_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/1v1_button.png'))
        exit_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/exit_button.png'))
        options_button_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/button_img/options_button.png'))
        
        
        #create button instances
        #Start menu buttons
        start_button = button.Button(600, 300, start_img, 0.5)
        rules_button = button.Button(600, 400, rules_button_img, 0.5)
        options_button = button.Button(600, 500, options_button_img, 0.5)
        exit_button = button.Button(600, 600, exit_button_img, 0.5)
        
        #Game mode menu buttons
        singlePlay_button = button.Button(600, 200, singlePlay_button_img, 0.2)
        multiplay_button = button.Button(600, 300, multiplay_button_img, 0.2)
        back = button.Button(80, 700, homescreen_button_img, 0.5)
        
        start_menu = "main"
        
        # Enter the main event loop
        running = True
        while running:
            # Fill the screen with white color
            screen.fill((255, 255, 255))
            
            if start_menu == "main":
                # Draw the button
                start_button.draw(screen)
                rules_button.draw(screen)
                options_button.draw(screen)
                exit_button.draw(screen)
                        
            if start_menu == "play":
                singlePlay_button.draw(screen)
                multiplay_button.draw(screen)
                back.draw(screen)
                        
            if start_menu == "rules":
                rules_img = pg.image.load(os.path.join(cwd, 'main/interface/Img/Rules.png'))
                rules_img = pg.transform.scale(rules_img,(600,600))
                rules_img_rect = rules_img.get_rect()
                rules_img_rect.center = ((400//1,000//2))
                screen.blit(rules_img,(400,50))
                back.draw(screen)
                
            if start_menu == "single_player":
                playerVplayer_button.draw(screen)
                playerVplayerVplayer_button.draw(screen)
                player2Vplayer2_button.draw(screen)
                    
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if start_menu == "main":
                        if start_button.is_clicked(event):
                            print("play")
                            start_menu = "play"
                        elif rules_button.is_clicked(event):
                            start_menu = "rules"
                        elif options_button.is_clicked(event):
                            start_menu = "options"
                        elif exit_button.is_clicked(event):
                            running = False
                    elif start_menu == "play":
                        if singlePlay_button.is_clicked(event):
                            start_menu = "single_player"
                        elif multiplay_button.is_clicked(event):
                            print("multiplay")
                        elif back.is_clicked(event):
                            # print("time")
                            start_menu = "main"
                    elif start_menu == "rules":
                        if back.is_clicked(event):
                            # print("time")
                            start_menu = "main"
                    elif start_menu == "single_player":
                        if playerVplayer_button.is_clicked(event):
                            print("1v1")
                        elif playerVplayerVplayer_button.is_clicked(event):
                            print("1v1v1")
                        elif player2Vplayer2_button.is_clicked(event):
                            print("2v2")
            
            # Add your code for drawing or updating the window here
            
            # Update the display
            pg.display.update()

        # Quit Pygame
        pg.quit()


