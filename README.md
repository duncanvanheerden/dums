# dums

#A wacky take on the original dominoes game.


##How the game works:

- when the game is run it prompts a user to select how many players will be participating and what  the score limit should be

- then cards are generated, shuffled and distributed evenly and according to the amount of players

- the round begins and the first player is prompted to select a card from their deck of cards and is able to place the card on either side of the game board if they have a valid card else they will be prompted that they are unable to play 

- the first player to run out of cards is allocated a point incrementing the amount of wins the player has, if both values of the players last card is equal to that of the numbers at both ends of the board or if no-one is able to play, the total of the numbers on their remaining cards will be compared to the other players totals, whoever has the lowest total will have their points incremented by 2 and the player is deemed winner of the round

- after a player wins a round, the game then restarts a new round with newly shuffled cards and the first player is once more prompted to select a card to place on the board 

- this continues until one player wins enough rounds equal to that of the score limit, the player is deemed winner of the game and the game end


##Running Unit Tests

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