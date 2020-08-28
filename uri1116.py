n = int(input())
lista = []
for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        a = 'divisao impossivel'
        lista.append(a)
    else:
        b = f'{x / y:.1f}'
        lista.append(b)

for j in lista:
    print(j)
