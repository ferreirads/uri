soma = 0
contador = 0

while True:
    a = float(input())
    if 0 <= a <= 10:
        soma = soma + a
        contador = contador + 1
        if contador == 2:
            print('media = {:.2f}'.format(soma / 2))
            print('novo calculo (1-sim 2-nao)')
            num = int(input())
            while num != 2 and num != 1:
                print('novo calculo (1-sim 2-nao)')
                num = int(input())
            if num == 1:
                contador = 0
                soma = 0
            elif num == 2:
                break
    else:
        print('nota invalida')
