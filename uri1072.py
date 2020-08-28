n = int(input())
contador1 = 0
contador2 = 0
while 0 < n < 10000:
    x = int(input())
    if 10 <= x <= 20:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1
    n = n - 1

print('{} in'.format(contador1))
print('{} out'.format(contador2))
