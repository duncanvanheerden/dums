def sort_play_order(all_player_hands,first_to_play):
    """
    sort the play order, making the player with the card (6,6) player 1/ first to play
    """
    all_player_hands.remove(first_to_play)
    all_player_hands.insert(0,first_to_play)
    return all_player_hands