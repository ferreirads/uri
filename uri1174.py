A = []
for i in range(100):
    n = float(input())
    A.append(n)
    if n <= 10:
        print('A[{}] = {:.1f}'.format(i, n))
