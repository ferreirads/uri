while True:
    x = int(input())
    soma = 0
    cont = 0
    if x == 0:
        break
    while True:
        if x % 2 == 0:
            soma = soma + x
            cont = cont + 1
        elif cont == 5:
            break
        x = x + 1
    print(soma)
