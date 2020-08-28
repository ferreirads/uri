x = float(input())

N = []

for i in range(100):
    N.append(x)
    x = x / 2
for a, b in enumerate(N):
    print('N[{}] = {:.4f}'.format(a, b))

