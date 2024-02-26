import tkinter as tk
from tkinter import messagebox

# Initialize the game board: a 3x3 list of strings
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def click(row, col):
    global current_player
    if board[row][col] == "" and not check_winner():
        board[row][col] = current_player
        color = "red" if current_player == "X" else "blue"
        buttons[row][col].config(text=str(current_player), fg=color)
        
        winning_cells = check_winner()
        if winning_cells:
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            highlight_winner(winning_cells)
            ask_to_reset()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            ask_to_reset()
        else:
            current_player = "O" if current_player == "X" else "X"
        
def highlight_winner(winning_cells):
    for cell in winning_cells:
        row, col = cell
        buttons[row][col].config(bg='yellow')  # Change background to yellow for the winning line

def ask_to_reset():
    # Optionally, ask the user if they want to play again or just reset the game directly
    response = messagebox.askyesno("Play Again?", "Would you like to play again?")
    if response:
        reset_game()

        
def check_winner():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return [(i, 0), (i, 1), (i, 2)]
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '':
            return [(0, i), (1, i), (2, i)]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return [(0, 2), (1, 1), (2, 0)]
    return []


def check_draw():
    return all("" not in row for row in board)

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg='light green')


def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='', fg='black', bg='light green')



# Create buttons for the game board
buttons = {}
for row in range(3):
    buttons[row] = {}

for row in range(3):
    for col in range(3):
        button = tk.Button(root, text='', font=('normal', 40), width=5, height=2,
                           command=lambda r=row, c=col: click(r, c),
                           bg='light green', activebackground='light green')
        button.grid(row=row, column=col)
        buttons[row][col] = button
        
root.mainloop()