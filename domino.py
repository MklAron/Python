import random


def tabla_letrehoz():
    return [[-1 for _ in range(8)] for _ in range(8)]

def is_valid(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

def lerak(tabla, ures_x, ures_y):
    domino_id = 0
    for i in range(8):
        for j in range(8):
            if (i, j) == (ures_x, ures_y) or tabla[i][j] != -1:
                continue
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx1, ny1 = i + dx, j + dy
                nx2, ny2 = i + 2 * dx, j + 2 * dy
                if is_valid(nx1, ny1, tabla) and is_valid(nx2, ny2, tabla):
                    tabla[i][j] = tabla[nx1][ny1] = tabla[nx2][ny2] = domino_id
                    domino_id += 1
                    break

def print_tabla(board):
    for row in board:
        print(" ".join(f"{cell:2}" if cell != -1 else " ." for cell in row))

def main():
    tabla = tabla_letrehoz()
    ures_x, ures_y = random.randint(0, 7), random.randint(0, 7)
    tabla[ures_x][ures_y] = -2
    lerak(tabla, ures_x, ures_y)
    print_tabla(tabla)

if __name__ == "__main__":
    main()