num = 1
contador = 0
while num <= 6:
    numero = float(input())
    if numero > 0:
        contador = contador + 1
    num = num + 1

print('{} valores positivos'.format(contador))
