numero = 1
contador = 0
lista = []
while numero <= 6:
    n = float(input())
    if n > 0:
        contador = contador + 1
        lista.append(n)
    numero = numero + 1

media = 0
for x in lista:
    media = media + x

nova_media = media / contador
print('{} valores positivos'.format(contador))
print('{:.1f}'.format(nova_media))
