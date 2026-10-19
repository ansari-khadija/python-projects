
# 🎮 Tic-Tac-Toe Game
# Hashtags: #Python #TicTacToe #PythonProjects #Coding

def print_board(board):
    print()
    for i in range(3):
        print(" " + " | ".join(board[i * 3:i * 3 + 3]))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True

    return False


def play_game():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("🎮 Welcome to Tic-Tac-Toe!")
    print("Choose a position from 1 to 9.")

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter position: ")

        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Invalid input! Choose a number from 1 to 9.")
            continue

        position = int(move) - 1

        if board[position] in ("X", "O"):
            print("That position is already taken!")
            continue

        board[position] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if all(cell in ("X", "O") for cell in board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
