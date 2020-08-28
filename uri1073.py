n = int(input())

if 5 < n < 2000:
    for i in range(0, n + 1, 2):
        if i != 0:
            multiplica = i ** 2
            print('{}^2 = {}'.format(i, multiplica))
