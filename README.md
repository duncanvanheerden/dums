# Dums

A wacky take on the original dominoes game.This repository contains a Dominoes game implemented in [Python]. The game allows players to play unique way of playing Dominoes against a computer opponent. It provides a user-friendly interface and implements the South African rules of playing.

## Features

- Play against a computer opponent
- Interactive and intuitive user interface
- Standard rules of Dominoes
- Score tracking and game statistics
- Customizable settings (e.g., difficulty level, game mode)
- Save and load game functionality
- Sound effects and animations (optional)

## How to Play

1. The game starts with a set of domino tiles shuffled and each player being dealt a hand of tiles.

2. The players take turns placing one of their tiles on the board. The tile must be placed adjacent to an existing tile, matching the number of pips on the adjacent sides.

3. If a player cannot make a valid move, they must draw from the boneyard until they either have a playable tile or the boneyard is empty.

4. The game continues until one of the players has no more tiles or neither player can make a move.

5. The player who played all their tiles or has the fewest remaining tiles wins the round. Points are awarded based on the sum of the pips on the opponent's remaining tiles.

6. The game can be played in multiple rounds, and the player with the highest total score at the end wins the game.

7. Enjoy playing Dominoes!

## Rules

The Dominoes game follows the standard rules of play. Here are some key rules:

- Each tile has two sides, with each side containing a certain number of pips.

- Tiles are placed end-to-end, with matching sides touching each other.

- If a player cannot make a move, they must draw from the boneyard until they have a playable tile or the boneyard is empty.

- If the boneyard is empty and neither player can make a move, the game ends.

- Scoring is based on the sum of pips on the opponent's remaining tiles at the end of each round.

- The game can be played in multiple rounds, and the player with the highest total score at the end wins.

## A wacky take on the original dominoes game.

Running Unit Tests

### How the game works:

- When the game is run it prompts a user to select how many players will be participating and what  the score limit should be.

- Cards are then generated, shuffled and distributed evenly and according to the amount of players.

- The round begins and the first player is prompted to select a card from their deck of cards and is able to place the card on either side of the game board if they have a valid card else they are unable to play.

- The first player to run out of cards is allocated a point incrementing the amount of wins the player has, if both values of the players last card is equal to that of the numbers at both ends of the board or if no-one is able to play, the total of the numbers on their remaining cards will be compared to the other players totals, whoever has the lowest total will have their points incremented by 2 and the player is deemed winner of the round.

- After a player wins a round, the game then restarts a new round with newly shuffled cards and the next player in the order is made the first player and is prompted to select a card to place on the board. 

- This continues until one player wins enough rounds equal to that of the score limit, the player is deemed winner of the game and the game ends.