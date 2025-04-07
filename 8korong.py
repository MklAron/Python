def megfordit(arr, k):
    arr[:k] = arr[:k][::-1]


def legnagyobb(arr, n):
    return arr.index(max(arr[:n]))


def rendez(arr):
    n = len(arr)
    for i in range(n, 1, -1):
        max_index = legnagyobb(arr, i)
        if max_index != i - 1:
            if max_index != 0:
                megfordit(arr, max_index + 1)
            megfordit(arr, i)
        print(arr)
    return arr

korongok = [6, 7, 3, 2, 8, 5, 4, 1]
print("Kezdő sorrend: ", korongok)
eredmeny = rendez(korongok)
print("Rendezett sorrend:", eredmeny)
