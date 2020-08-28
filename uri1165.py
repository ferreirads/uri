n = int(input())

for i in range(n):
    x = int(input())
    cont = 0
    lista = []
    while x >= cont:
        cont = cont + 1
        if x % cont == 0:
            lista.append(cont)
    if lista[0] == 1 and lista[1] == x:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
