n = int(input())
lista = []
while 1 <= n <= 1000:
    if n % 2 != 0:
        lista.append(n)
    n = n - 1
lista.sort()
for x in lista:
    print(x)
