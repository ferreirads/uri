t = int(input())

if 1 <= t <= 3000:
    for i in range(t):
        pa, pb, g1, g2 = input().split()
        pa = int(pa)
        pb = int(pb)
        g1 = float(g1)
        g2 = float(g2)
        cont = 0
        while pa <= pb:
            crescimentoA = int((pa * g1) // 100)
            crescimentoB = int((pb * g2) // 100)
            pa = pa + crescimentoA
            pb = pb + crescimentoB
            cont = cont + 1
            if cont > 100:
                print('Mais de 1 seculo.'.format(cont))
                break
        if cont <= 100:
            print('{} anos.'.format(int(cont)))
