a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

maior = (a + c + abs(a - c)) // 2
maior2 = (maior + b + abs(maior - b)) // 2

print('{} eh o maior'.format(maior2))
