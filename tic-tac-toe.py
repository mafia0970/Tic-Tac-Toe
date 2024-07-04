import tkinter as tk
from tkinter import messagebox

# Initialize tkinter
win = tk.Tk()
win.title('Tic-Tac-Toe')
win.geometry("300x420")
win.resizable(width=False, height=False)

# Global variables
flag1 = 0  # used to decide the turn (0 for Player 1, 1 for Player 2)
score1 = {
    "player1": 0,
    "player2": 0
}
count = 0
game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def ask_yes_no():
    response = messagebox.askquestion("Confirmation", "Do you want to Play?")
    if response == 'yes':
        reset_game()        
    else:
        win.destroy()

def check_winner():
    global game
    # Check rows and columns
    for i in range(3):
        if (game[i][0] == game[i][1] == game[i][2] == 1) or (game[i][0] == game[i][1] == game[i][2] == 2):
            show_winner(game[i][0])
            return
        if (game[0][i] == game[1][i] == game[2][i] == 1) or (game[0][i] == game[1][i] == game[2][i] == 2):
            show_winner(game[0][i])
            return
    # Check diagonals
    if (game[0][0] == game[1][1] == game[2][2] == 1) or (game[0][0] == game[1][1] == game[2][2] == 2):
        show_winner(game[0][0])
        return
    if (game[0][2] == game[1][1] == game[2][0] == 1) or (game[0][2] == game[1][1] == game[2][0] == 2):
        show_winner(game[0][2])
        return
    # Check for a tie
    if count == 9:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        reset_game()

def show_winner(player):
    global game
    global score1
    if player == 1:
        score1["player1"] += 1
        messagebox.showinfo("Tic-Tac-Toe", "Player 1 wins!")
    elif player == 2:
        score1["player2"] += 1
        messagebox.showinfo("Tic-Tac-Toe", "Player 2 wins!")

    # Update score display
    score.config(text=f"Player1 = {score1['player1']} || Player2 = {score1['player2']}")

    # Ask if the players want to play again
    ask_yes_no()

def reset_game():
    global game, count, flag1
    # Reset game variables
    count = 0
    flag1 = 0
    game = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Clear button texts
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")

# Function to handle button clicks
def change_text(btn, i, j):
    global count, flag1, game
    if game[i][j] == 0:
        count += 1
        if flag1 == 0:
            btn.config(text="X")
            game[i][j] = 1
            flag1 = 1
            flag.config(text="Player 2")
        else:
            btn.config(text="O")
            game[i][j] = 2
            flag1 = 0
            flag.config(text="Player 1")

    # Check for winner/tie after each move
    check_winner()

# GUI setup
frame = tk.Frame(win)
frame.grid(row=0, column=0)

flag = tk.Label(frame, text="Player 1", background="black", foreground="white", width=42, height=2)
flag.grid(row=0, column=0)

frame2 = tk.Frame(win)
frame2.grid(row=2, column=0)

score = tk.Label(frame, text=f"Player1 = {score1['player1']}                ||                   Player2 = {score1['player2']}")
score.grid(row=1, column=0)

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame2, text=" ", width=10, height=7, padx=9, pady=2, background="black", foreground="white",
                        command=lambda i=i, j=j: change_text(buttons[i][j], i, j))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

win.mainloop()
