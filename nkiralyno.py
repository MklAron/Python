N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    return True

def solve_n_queens(board, col):
    if col >= N:
        print_solution(board)
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = True
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = False
    
    return res

def solve():
    board = [[False] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("Nincs megoldas")

solve()
