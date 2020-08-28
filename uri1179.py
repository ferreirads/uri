par = []
impar = []
cont = 0
cont2 = 0
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        cont = cont + 1
        if cont == 5:
            for a, b in enumerate(par):
                print('par[{}] = {}'.format(a, b))
            par.clear()
            cont = 0
    elif n % 2 != 0:
        impar.append(n)
        cont2 = cont2 + 1
        if cont2 == 5:
            for c, d in enumerate(impar):
                print('impar[{}] = {}'.format(c, d))
            impar.clear()
            cont2 = 0
for j, k in enumerate(impar):
    print('impar[{}] = {}'.format(j, k))
for p, m in enumerate(par):
    print('par[{}] = {}'.format(p, m))
