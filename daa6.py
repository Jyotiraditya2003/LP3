#n queens
N = 8 
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    return True

def solve_queens(board, col):
    if col >= N:
        print("Final 8-Queens Matrix:")
        print_board(board)
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1 

            if solve_queens(board, col + 1):
                return True

            board[row][col] = 0

    return False

if __name__ == "__main__":
    board = [[0 for _ in range(N)] for _ in range(N)]
    first_row, first_col = 0, 0
    board[first_row][first_col] = 1

    print("Initial board with first Queen placed:")
    print_board(board)

    if not solve_queens(board, first_col + 1):
        print("Solution does not exist.")

#TC O(N!)
#SC O(N^2)