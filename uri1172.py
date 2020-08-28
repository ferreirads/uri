x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(x)):
    n = int(input())
    if n <= 0:
        n = 1
    print('X[{}] = {}'.format(i, n))
