import pygame
pygame.init()

WIDTH, HEIGHT = 900 ,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dominos")

FPS = 60

WHITE = (205, 127, 50)

font = pygame.font.SysFont("arialwhite",70)

TEXT_COL = (255,248,220)

def draw_text(text, font , text_col, x , y):
    img = font.render(text, True , text_col)
    WIN.blit(img,(x, y))
    

def pygame_window():
    
    
    clock = pygame.time.Clock()
    run = True
    while run:
        WIN.fill(WHITE)
        draw_text("Welcome To DUMS", font , TEXT_COL, 250 , 50)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()
        
    pygame.quit()