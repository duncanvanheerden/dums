def sort_play_order(all_player_hands,first_to_play):
    """
    sort the play order, making the player with the card (6,6) player 1/ first to play
    """
    all_player_hands.remove(first_to_play)
    all_player_hands.insert(0,first_to_play)
    return all_player_hands


def milo(player_hand,game):
    """
    Determines if a players last card is able to be played 
    on either end of the gameboard list with each end of the players last card
    matching to that of the games

    returns True else False

    Args:
        player_hand (list): list of all remaining dominoes in player hand
        game (list): list of tuples played and displayed as the gameboard
    """    
    left_end_game = game[0][0]
    right_end_game = game[-1][-1]
    left_end_playercard = player_hand[0][0]
    right_end_playercard = player_hand[0][-1]

    if left_end_game == left_end_playercard and right_end_game == right_end_playercard:
        return True
    elif left_end_game == right_end_playercard and right_end_game == left_end_playercard:
        return True
    elif left_end_game == right_end_playercard and right_end_game == right_end_playercard:
        return True
    elif left_end_game == left_end_playercard and right_end_game == left_end_playercard:
        return True
    else:
        return False



