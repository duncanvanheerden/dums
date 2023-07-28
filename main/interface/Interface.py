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
        start_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/start_button.png'))
        rules_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/rules.png'))
        singlePlay_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/Single_player.png'))
        multiplay_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/Multiplayer.png'))
        homescreen_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/home_screen.png'))
        playerVplayer_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/1v1_button.png'))
        playerVplayerVplayer_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/1v1_button.png'))
        player2Vplayer2_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/1v1_button.png'))
        exit_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/exit_button.png'))
        options_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/options_button.png'))
        
        #create button instances
        #Start menu buttons
        start_button = button.Button(600, 300, start_img, 0.5)
        rules_button = button.Button(600, 400, rules_img, 0.5)
        options_button = button.Button(600, 500, options_img, 0.5)
        exit_button = button.Button(600, 600, exit_img, 0.5)
        
        #Game mode menu buttons
        singlePlay_button = button.Button(600, 200, singlePlay_img, 0.2)
        multiplay_button = button.Button(600, 300, multiplay_img, 0.2)
        homescreen = button.Button(500, 500, homescreen_img, 0.5)
        
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
                homescreen.draw(screen)
                        
            if start_menu == "rules":
                print("rules")
                
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
                        elif homescreen.is_clicked(event):
                            print("time")
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


