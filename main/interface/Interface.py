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
        width = 1300
        height = 600
        
        # Get current working directory
        cwd = os.getcwd()

        # Create the window display
        screen = pg.display.set_mode((width, height))

        # Set the title of the window
        pg.display.set_caption("My Pygame Window")
        
        #load button images
        start_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/start_btn.png'))
        rules_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/rules.png'))
        singlePlay_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/Single_player.png'))
        multiplay_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/Multiplayer.png'))
        homescreen_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/home_screen.png'))
        exit_img = pg.image.load(os.path.join(cwd, 'main/interface/Button/img/exit_button.png'))

        #create button instances
        start_button = button.Button(200, 0, start_img, 0.5)
        rules_button = button.Button(200, 200, rules_img, 1.2)
        singlePlay_button = button.Button(200, 200, singlePlay_img, 1.2)
        multiplay_button = button.Button(200, 400, multiplay_img, 1.2)
        homescreen = button.Button(200, 600, homescreen_img, 2)
        exit_button = button.Button(200, 400, exit_img, 0.5)
        
        start_menu = "main"
        
        # Enter the main event loop
        running = True
        while running:
            # Fill the screen with white color
            screen.fill((255, 255, 255))
            
            if start_menu == "main":
                # Draw the button
                if start_button.draw(screen):
                    print("play")
                    start_menu = "play"
                    pass
                
                if exit_button.draw(screen):
                    running = False
                    
                if rules_button.draw(screen):
                    start_menu = "rules"
            
            if start_menu == "play":
                
                if singlePlay_button.draw(screen):
                    print("singleplay")
                 
                if multiplay_button.draw(screen):
                    print("multiplay")
                    
                if homescreen.draw(screen):
                    start_menu = "main"
                    
            if start_menu == "rules":
                print("rules")
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # Add your code for drawing or updating the window here

            # Update the display
            pg.display.update()

        # Quit Pygame
        pg.quit()


# Create an instance of the Interface class
my_interface = Interface()

# Call the window method to create the Pygame window
my_interface.window()
