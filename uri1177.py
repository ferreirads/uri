T = int(input())
n = []
cont = 0
for i in range(1000):
    if cont > T - 1:
        cont = 0
    n.append(cont)
    cont = cont + 1
for a, b in enumerate(n):
    print('N[{}] = {}'.format(a, b))
