while True:
    lista = []
    x = int(input())
    if x == 0:
        break
    while x > 0:
        lista.append(x)
        x = x - 1
    lista.sort()
    print(' '.join(map(str, lista)))

