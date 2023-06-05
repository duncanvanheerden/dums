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


## Running Unit Tests

To run the unit tests in this project, make sure you have the following configurations set up:
Visual Studio Code Settings

    Open the project in Visual Studio Code.
    Press Ctrl + Shift + P (or Cmd + Shift + P on macOS) to open the command palette.
    Type "Preferences: Open Workspace Settings" and press Enter.
    In the workspace settings, ensure that the following settings are configured:

json

{
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "*test*.py"
    ],
    "python.testing.pytestEnabled": false
}

The above settings enable the unit testing framework for Python's unittest module and specify the arguments to be used when running the tests. The -s flag specifies the directory where the test files are located (./tests in this case), and the -p flag filters the test files based on a pattern (*test*.py in this case).
Running the Unit Tests

Once the Visual Studio Code settings are configured, you can run the unit tests by performing the following steps:

    Open the command palette in Visual Studio Code by pressing Ctrl + Shift + P (or Cmd + Shift + P on macOS).
    Type "Python: Discover Tests" and press Enter. This will discover the unit tests in the specified directory.
    Open the command palette again and type "Python: Run All Unit Tests" to execute all the discovered unit tests.