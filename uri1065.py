numero = 0
contador = 0
while numero < 5:
    n = int(input())
    if n % 2 == 0:
        contador = contador + 1
    numero = numero + 1

print('{} valores pares'.format(contador))
