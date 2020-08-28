N = []

for i in range(20):
    num = int(input())
    N.append(num)
N.reverse()
for j, k in enumerate(N):
    print('N[{}] = {}'.format(j, k))
