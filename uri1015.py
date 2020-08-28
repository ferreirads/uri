x0, y0 = input().split(' ')
x1, y1 = input().split(' ')
x0 = float(x0)
x1 = float(x1)
y0 = float(y0)
y1 = float(y1)

distancia = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** (1/2)

print('{:.4f}'.format(distancia))
