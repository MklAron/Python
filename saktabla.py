LEPES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]


def alkalmazhato(x, y, tabla):
    return 0 <= x < 8 and 0 <= y < 8 and tabla[x][y] == -1


def lep(x, y, tabla):
    lepesek = []
    for dx, dy in LEPES:
        nx, ny = x + dx, y + dy
        if alkalmazhato(nx, ny, tabla):
            count = sum(1 for mx, my in LEPES if alkalmazhato(nx + mx, ny + my, tabla))
            lepesek.append((count, nx, ny))
    lepesek.sort()
    return [(nx, ny) for _, nx, ny in lepesek]


def megold(x, y, lepes_szam, tabla):
    if lepes_szam == 60:
        for dx, dy in LEPES:
            nx, ny = x + dx, y + dy
            if (nx, ny) == (0, 1):
                return True
        return False

    for nx, ny in lep(x, y, tabla):
        tabla[nx][ny] = lepes_szam
        if megold(nx, ny, lepes_szam + 1, tabla):
            return True
        tabla[nx][ny] = -1

    return False


def megoldas():
    tabla = [[-1 for _ in range(8)] for _ in range(8)]
    sarok = [(0, 0), (0, 7), (7, 0), (7, 7)]
    for x, y in sarok:
        tabla[x][y] = -2
    start_x, start_y = 0, 1
    tabla[start_x][start_y] = 0

    if megold(start_x, start_y, 1, tabla):
        print("Megoldás:")
        for sor in tabla:
            print(" ".join(f"{num:2}" for num in sor))
    else:
        print("Nincs megoldás.")

megoldas()