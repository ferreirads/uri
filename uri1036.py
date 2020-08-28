import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (b ** 2) - (4 * a * c)

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    raiz = math.sqrt(delta)
    x1 = (- b + raiz) / (2 * a)
    x2 = (- b - raiz) / (2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
