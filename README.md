Tic Tac Toe in Python with Tkinter

This project is a simple implementation of the classic game Tic Tac Toe, built using Python and the Tkinter GUI library. It allows two players to play the game on a single computer, alternating turns between X and O.
Features

    A graphical user interface for easy interaction.
    Highlights the winning combination.
    Notifies players of the game outcome: win or draw.
    Option to restart the game once it is finished.

How to Run

To run the game, you will need Python installed on your computer. This game was developed with Python 3.x in mind. If you have Python installed, you can simply download the game and run it from your command line or terminal:

bash

python "Tic Tac Toe GUI_version.py"


Gameplay

    The game window consists of a 3x3 grid of buttons.
    Players take turns clicking on an empty square to make their move (Player 1 is X, Player 2 is O).
    The first player to align three of their symbols vertically, horizontally, or diagonally wins the game.
    If all squares are filled and no player has 3 symbols in a row, the game is a draw.
    Once the game concludes, a message box will pop up announcing the result and asking if players wish to play again.

Code Structure

The game logic is contained within a single Python script (Tic Tac Toe GUI_version.py) and includes functions to handle game logic, player actions, and the graphical user interface.

    click(row, col): Handles button click events, updates the game state, and checks for a win or draw.
    check_winner(): Checks the current state of the board for a winner.
    check_draw(): Checks for a draw (no empty spaces left).
    reset_game(): Resets the game board and player turns for a new game.
    highlight_winner(winning_cells): Highlights the winning combination on the board.

Dependencies

    Python 3.x
    Tkinter (usually comes with Python)
    
 Contributing

I love collaborating with fellow coders! If you have any improvements or features you'd like to suggest, please follow these steps to contribute to the Tic Tac Toe project:

1. **Fork the Project**: Click the 'Fork' button at the top right of the page to create your own copy of the project.

2. **Create your Feature Branch** (`git checkout -b feature/YourAmazingFeature`): Replace 'YourAmazingFeature' with a short name for the feature you're adding.

3. **Commit your Changes** (`git commit -m 'Add some YourAmazingFeature'`): Replace 'Add some YourAmazingFeature' with a message that describes what you've added or changed.

4. **Push to the Branch** (`git push origin feature/YourAmazingFeature`): Push your work back up to your fork.

5. **Open a Pull Request**: Navigate to the original project and click the "Pull requests" tab, then click "New pull request". Choose your branch and fill out the form. Please give as much information as necessary in the description.

Please make sure to update tests as appropriate. If you're adding a new function, include unit tests. Follow the PEP 8 coding style for consistency.

Open an issue if you have any questions or want to discuss a feature idea.

Thank you for your contributions!

Licence

Distributed under the MIT Licence.
See Licence for more information.

