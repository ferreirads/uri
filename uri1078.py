n = int(input())
if 2 < n < 1000:
    for i in range(1, 10 + 1):
        print('{} x {} = {}'.format(i, n, i * n))
