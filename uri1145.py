x, y = map(int, input().split())
lista = []
if 1 < x < 20 and x < y < 100000:
    for i in range(1, y + 1):
        lista.append(i)
        if len(lista) == x:
            print(' '.join(map(str, lista)))
            lista = []
