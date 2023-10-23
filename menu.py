import pygame
import sys


class Menu:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Main Menu')
        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        # Define fonts
        self.font = pygame.font.Font(None, 36)


    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)    

    # def main_menu(self, game):
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()

    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if self.play_rect.collidepoint(event.pos):
    #                     game.setup_game()

    #                 elif self.host_rect.collidepoint(event.pos):
    #                     # Add code to handle hosting a game
    #                     pass

    #                 elif self.join_rect.collidepoint(event.pos):
    #                     # Add code to handle joining a game
    #                     pass

    #         self.display_menu()

    def num_players_menu(self):
        num_players = None

        while num_players is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    for i in range(2, 5):
                        if self.player_buttons[i].collidepoint(event.pos):
                            num_players = i
                            break

            self.screen.fill(self.BLACK)

            # Create player number buttons
            self.player_buttons = {}
            for i in range(2, 5):
                self.player_buttons[i] = pygame.draw.rect(self.screen, self.WHITE, (300, 200 + (i-2)*75, 200, 50))
                self.draw_text(f"{i} Players", 400, 225 + (i-2)*75)

            pygame.display.flip()

        return num_players

    def score_limit_menu(self):
        score_limit = None

        while score_limit is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    for i in range(1, 6):
                        if self.score_buttons[i].collidepoint(event.pos):
                            score_limit = i
                            break

            self.screen.fill(self.BLACK)

            # Create score limit buttons
            self.score_buttons = {}
            for i in range(1, 6):
                self.score_buttons[i] = pygame.draw.rect(self.screen, self.WHITE, (300, 150 + (i-1)*75, 200, 50))
                self.draw_text(f"Score Limit: {i}", 400, 175 + (i-1)*75)

            pygame.display.flip()

        return score_limit

    def display_menu(self):
        self.screen.fill(self.BLACK)

        # Create play button
        self.play_rect = pygame.draw.rect(self.screen, self.WHITE, (300, 200, 200, 50))
        self.draw_text("Local Play", 400, 225)

        # Create host button
        self.host_rect = pygame.draw.rect(self.screen, self.WHITE, (300, 275, 200, 50))
        self.draw_text("Host Game", 400, 300)

        # Create join button
        self.join_rect = pygame.draw.rect(self.screen, self.WHITE, (300, 350, 200, 50))
        self.draw_text("Join Game", 400, 375)

        pygame.display.flip()


    def get_username(self):
        """
        Display a prompt to get the username from the player.

        Returns:
            str: The entered username.
        """
        input_box = pygame.Rect(300, 200, 200, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        font = pygame.font.Font(None, 36)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill(self.WHITE)
            width = 200 if len(text) < 8 else 300
            input_box.w = width
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            self.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(self.screen, color, input_box, 2)

            self.draw_text("Enter Your Username", 400, 100)
            self.draw_text("Press ENTER to Submit", 400, 400)

            pygame.display.flip()
            clock.tick(30)


    def display_deck(self, player):
        self.screen.fill(self.BLACK)

        button_width = 50
        button_height = 30
        button_padding = 10

        player_deck = player.deck

        total_width = (button_width + button_padding) * len(player_deck)
        start_x = (self.screen.get_width() - total_width) // 2

        chosen_card = None

        # Set the position 10 pixels from the bottom of the screen
        y_position = self.screen.get_height() - 10 - button_height

        # Create buttons for each card in the player's deck
        for index, card in enumerate(player_deck):
            x_position = start_x + index * (button_width + button_padding)

            card_button = pygame.draw.rect(self.screen, self.WHITE, (x_position, y_position, button_width, button_height))

            card_text = f"{card[0]}-{card[1]}"
            self.draw_text(card_text, x_position + button_width // 2, y_position + button_height // 2)

        pygame.display.flip()

        # Wait for player to select a card
        while chosen_card is None:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for index, card in enumerate(player_deck):
                        x_position = start_x + index * (button_width + button_padding)

                        card_rect = pygame.Rect(x_position, y_position, button_width, button_height)

                        if card_rect.collidepoint(event.pos):
                            chosen_card = player_deck[index]
                            break

        return chosen_card  # Return the chosen card value

        

            
                
