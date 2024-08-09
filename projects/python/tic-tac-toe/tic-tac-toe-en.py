# Import the system function from the os module
from os import system

# Create the game board using a list of lists
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Display a welcome message at the start of the game
def welcome_message():
    print("Welcome to the Tic Tac Toe game!\n")

# Draw the game board with the current symbols
def draw_board():
    print(''' {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}'''.format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))

# Update the board with the player's symbol at the specified row and column
def update_board(row, column, player_symbol):
    board[row][column] = player_symbol

# Get the player's name based on their symbol
def get_player_name(player_symbol):
    return "Player One" if player_symbol == "X" else "Player Two"

# Check for a victory by the current player
def check_victory(player_symbol):
    winning_combinations = [
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)]
    ]
    for combination in winning_combinations:
        if all(board[x][y] == player_symbol for x, y in combination):
            player_name = get_player_name(player_symbol)
            print("\n{} has won! The game has ended".format(player_name))
            return True
    return False

# Prompt for the position on the board where the player wants to place their symbol
def prompt_board_position(player_symbol):
    try:
        while True:
            row = int(input("\nEnter the row [1-3] where you want to place '{}': ".format(player_symbol))) - 1
            column = int(input("Enter the column [1-3] where you want to place '{}': ".format(player_symbol))) - 1
            if 0 <= row <= 2 and 0 <= column <= 2:
                if board[row][column] == " ":
                    system("cls") # Clear the console (Windows)
                    return row, column
                else:
                    print("ERROR: You cannot place a symbol on top of another symbol.")
            else:
                print("ERROR: Please enter only numbers between 1 and 3.")
    except:
        print("ERROR: Please enter only numbers between 1 and 3.")
        row, column = prompt_board_position(player_symbol)
        return row, column

# Display the end game message in case of a tie
def tie_game_message():
    input("\nCongratulations, players! The game has ended in a tie.")
    exit()

# Execute the turn of the current player
def player_turn(player_symbol):
    player_name = get_player_name(player_symbol)
    print("\n{}'s Turn.".format(player_name))
    row, column = prompt_board_position(player_symbol)
    update_board(row, column, player_symbol)
    draw_board()
    if check_victory(player_symbol):
        exit()

# Start the game
def start_game():
    welcome_message()
    draw_board()
    for i in range(9):
        player_symbol = "X" if i % 2 == 0 else "O"
        player_turn(player_symbol)
    tie_game_message()

# Start the match
if __name__ == "__main__":
    start_game()

# Marc Delgado Ferreres