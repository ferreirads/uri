n = int(input())

for i in range(n):
    x = int(input())
    cont = 0
    soma = 0
    while True:
        cont = cont + 1
        if x % cont == 0:
            if cont == x:
                break
            soma = soma + cont
    if soma == x:
        print('{} eh perfeito'.format(x))
    elif soma != x:
        print('{} nao eh perfeito'.format(x))
