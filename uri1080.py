n = 100
lista = [0]
while n > 0:
    numero = int(input())
    lista.append(numero)
    n = n - 1

maximo = max(lista)
posicao = lista.index(maximo)

print(maximo)
print(posicao)
