n = int(input())
lista = []
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    soma = 0
    if x < y:
        for k in range(x + 1, y):
            if k % 2 != 0:
                soma = soma + k
    elif x > y:
        for k in range(y + 1, x):
            if k % 2 != 0:
                soma = soma + k
    lista.append(soma)

for a in lista:
    print(a)
