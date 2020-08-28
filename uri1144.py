n = int(input())
num = 0
for i in range(n):
    num = num + 1
    quadrado = num ** 2
    cubo = num ** 3
    print(f'{num} {quadrado} {cubo}')
    print(f'{num} {quadrado + 1} {cubo + 1}')

