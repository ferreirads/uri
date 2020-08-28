n = int(input())
soma = 0
cont = 0
for i in range(n):
    a, b = map(int, input().split())
    while True:
        if a % 2 != 0:
            soma = soma + a
            cont = cont + 1
            if cont == b:
                break
        a = a + 1
    print(soma)
    soma = 0
    cont = 0
