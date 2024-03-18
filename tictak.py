
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
         return True

    for col in range(3):
     if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
            return True

    if all(board[i][2 - i] == player for i in range(3)):
             return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Please enter row and column numbers between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That cell is already occupied. Please choose another.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
