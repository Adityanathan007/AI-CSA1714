def display_board(board):
    for row in range(3):
        print(" " + " | ".join(board[row * 3 : row * 3 + 3]))
        if row < 2:
            print("---+---+---")


def get_winner(board):
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6),             # Diagonals
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return board[a]

    return None


def play_game():
    board = [str(number) for number in range(1, 10)]
    current_player = "X"

    while True:
        print()
        display_board(board)
        choice = input(f"Player {current_player}, choose a square (1-9): ").strip()

        if choice not in "123456789" or len(choice) != 1:
            print("Enter a number from 1 to 9.")
            continue

        position = int(choice) - 1

        if board[position] in ("X", "O"):
            print("That square is taken. Choose another.")
            continue

        board[position] = current_player

        winner = get_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break

        if all(cell in ("X", "O") for cell in board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    print("Tic Tac Toe — choose a square by its number.")
    play_game()
