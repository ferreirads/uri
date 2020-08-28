numerador = 3
denominador = 2
soma = 0
while True:
    soma = soma + (numerador / denominador)
    numerador = numerador + 2
    denominador = denominador * 2
    if numerador == 39:
        break
s = 1 + soma
print('{:.2f}'.format(s))
