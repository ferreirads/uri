n = int(input())
lista = []
while n > 0:
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    media = ((a * 2) + (b * 3) + (c * 5)) / 10
    lista.append(media)
    n = n - 1

for i in lista:
    print('{:.1f}'.format(i))
