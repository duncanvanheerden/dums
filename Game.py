def selecting_game_mode():
    
    while True:
        
        users_input = input("(1)Dums in terminal or (2)Dums in pygame: ")
        
        
        if users_input == "1":
            import dums_in_terminal.dums 
            break
            

        elif users_input == "2":
            import dums_in_pygame.dums_pygame
            break
        else:
            pass
            
            
            
if __name__ == '__main__':
    selecting_game_mode()