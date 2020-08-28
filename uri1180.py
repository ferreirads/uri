n = int(input())
x = []
a = list(map(int, input().split()))
for i in range(n):
    x.append(a[i])
for j, k in enumerate(x):
    if k == min(x):
        print('Menor valor: {}'.format(k))
        print('Posicao: {}'.format(j))
