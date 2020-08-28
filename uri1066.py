num = 0
positivo = 0
negativo = 0
pares = 0
impares = 0

while num < 5:
    n = int(input())
    if n > 0:
        positivo = positivo + 1
    elif n < 0:
        negativo = negativo + 1
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    num = num + 1

print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))
