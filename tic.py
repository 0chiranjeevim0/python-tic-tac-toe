# Initialize the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Variable to keep track of the current player
current_player = "X"

# Function to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to play a turn
def play_turn():
    global current_player
    position = int(input("Choose a position from 1-9: ")) - 1
    if board[position] == "-":
        board[position] = current_player
        display_board()
        if check_win():
            print(current_player + " wins!")
            return True
        elif check_tie():
            print("Tie game!")
            return True
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
    else:
        print("That position is already taken. Please choose another position.")
    return False

# Function to check if a player has won
def check_win():
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return True
    else:
        return False

# Function to check if the game is tied
def check_tie():
    if "-" not in board:
        return True
    else:
        return False

# Function to start the game
def start_game():
    display_board()
    while True:
        if play_turn():
            break

# Start the game
start_game()
