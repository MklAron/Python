from collections import deque

kezdoAllapot = [
    [2, 2, 2],
    [-1, 0, -1],
    [0, 0, -1],
    [-1, 0, -1],
    [1, 1, 1]
]

iranyok = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def keres(tabla, ertek):
    pozicio = []
    for r in range(len(tabla)):
        for c in range(len(tabla[r])):
            if tabla[r][c] == ertek:
                pozicio.append((r, c))
    return pozicio


def kiiratas(tabla):
    symb = {-1: 'X',0: '-', 1: 'P', 2: 'Z'}
    for row in tabla:
        print(" ".join(symb[cell] for cell in row))
    print("\n" + "-" * 10)

def cserel(tabla):
    kezdo_allapot = (tuple(keres(tabla, 1)), tuple(keres(tabla, 2)))
    cel_allapot = (tuple(keres(tabla, 2)), tuple(keres(tabla, 1)))

    queue = deque([(tabla, [], kezdo_allapot)])
    chk = set()
    chk.add(kezdo_allapot)

    while queue:
        jelenlegi_tabla, lepesek, (piros_poz, zold_poz) = queue.popleft()

        if (piros_poz, zold_poz) == cel_allapot:
            return lepesek

        ures_mezok = keres(jelenlegi_tabla, 0)
        for r, c in ures_mezok:
            for dr, dc in iranyok:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(tabla) and 0 <= nc < len(tabla[nr]) and jelenlegi_tabla[nr][nc] in [1, 2]:
                    uj_tabla = [row[:] for row in jelenlegi_tabla]
                    uj_tabla[r][c], uj_tabla[nr][nc] = uj_tabla[nr][nc], uj_tabla[r][c]
                    uj_piros_poz = tuple(keres(uj_tabla, 1))
                    uj_zold_poz = tuple(keres(uj_tabla, 2))
                    kovetkezo_lepes = lepesek + [(uj_tabla, ((nr, nc), (r, c)))]
                    uj_allapot = (uj_piros_poz, uj_zold_poz)
                    if uj_allapot not in chk:
                        chk.add(uj_allapot)
                        queue.append((uj_tabla, kovetkezo_lepes, uj_allapot))
    return None

if __name__ == '__main__':
    megoldas = cserel(kezdoAllapot)
    print("Megoldás lépései:")
    if megoldas:
        for lepes in megoldas:
            tabla, lep = lepes
            print(f"Lép: {lep[0]} --> {lep[1]}")
            kiiratas(tabla)
    else:
        print("Nincs megoldás!")
