n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input())

for i in range(len(n)):
    n.insert(i, num)
    print('N[{}] = {}'.format(i, num))
    num = num * 2
