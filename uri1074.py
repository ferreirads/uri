n = int(input())
lista = []
while 0 < n < 10000:
    x = int(input())
    lista.append(x)
    n = n - 1

for i in lista:
    if i < 0 and i % 2 == 0:
        print('EVEN NEGATIVE')
    elif i < 0 and i % 2 != 0:
        print('ODD NEGATIVE')
    elif i > 0 and i % 2 == 0:
        print('EVEN POSITIVE')
    elif i > 0 and i % 2 != 0:
        print('ODD POSITIVE')
    else:
        print('NULL')
