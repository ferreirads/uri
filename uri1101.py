while True:
    lista = []
    m, n = map(int, input().split())
    if m <= 0 and n <= 0:
        break
    if m > n:
        m, n = n, m
    for i in range(m, n + 1):
        lista.append(i)
    soma = f'Sum={sum(lista)}'
    lista.append(soma)
    print(' '.join(map(str, lista)))
