import pygame

pygame.init()

WIDTH, HEIGHT = 900 ,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dominos")

FPS = 60

BROWN = (205, 127, 50)

font = pygame.font.SysFont("arialwhite",70)

start_img = pygame.image.load("Buttons/Start.png").convert_alpha()


TEXT_COL = (255,248,220)

def draw_text(text, font , text_col, x , y):
    """Draws text on the game window
    * Takes text parameter what the text will show
    * Takes font for type of font
    * Takes text_col for color of text
    * X and Y parameters is where the text will be shown on pygame window"""
    
    img = font.render(text, True , text_col)
    #Blit prints the text out on window
    WIN.blit(img,(x, y))
    

def pygame_window():
    """Main game function where the Pygame runs"""
    
    
    clock = pygame.time.Clock()
    run = True
    
    #Event handler
    while run:
        WIN.fill(BROWN)
        draw_text("Welcome To DUMS", font , TEXT_COL, 250 , 50)
        clock.tick(FPS)
        
        for event in pygame.event.get():
            #Quit game
            if event.type == pygame.QUIT:
                run = False
                
        #Updates the game window        
        pygame.display.update()
        
    pygame.quit()
    

if __name__ != '__main__':
    pygame_window()