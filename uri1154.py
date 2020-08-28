cont = 0
soma = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    cont = cont + 1
    soma = soma + idade
media = soma / cont
print('{:.2f}'.format(media))
