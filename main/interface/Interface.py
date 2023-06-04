import pygame as pg


class Interface():

    def __init__(self):
        pg.init()

    def window(self):
        # Set the dimensions of the window
        width = 1300
        height = 600

        # Create the window display
        screen = pg.display.set_mode((width, height))

        # Set the title of the window
        pg.display.set_caption("My Pygame Window")

        # Enter the main event loop
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # Fill the screen with white color
            screen.fill((255, 255, 255))

            # Add your code for drawing or updating the window here

            # Update the display
            pg.display.update()

        # Quit Pygame
        pg.quit()


# Create an instance of the Interface class
my_interface = Interface()

# Call the window method to create the Pygame window
my_interface.window()
