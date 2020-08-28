soma = 1
soma2 = 0
while True:
    soma = soma + 1
    soma2 = soma2 + (1/soma)
    if soma == 100:
        break

s = 1 + soma2
print('{:.2f}'.format(s))
