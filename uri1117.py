soma = 0
contador = 0
while True:
    a = float(input())
    n = 0
    if 0 <= a <= 10:
        contador = contador + 1
        soma = soma + a
        if contador == 2:
            print('media = {:.2f}'.format(soma / 2))
            break
    else:
        print('nota invalida')
