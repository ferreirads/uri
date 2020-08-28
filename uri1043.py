a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a > 0 and b > 0 and c > 0:
    perimetro_triangulo = a + b + c
    if abs(b - c) < a < b + c:
        print('Perimetro = {:.1f}'.format(perimetro_triangulo))

    elif abs(a - c) < b < a + c:
        print('Perimetro = {:.1f}'.format(perimetro_triangulo))

    elif abs(a - b) < c < a + b:
        print('Perimetro = {:.1f}'.format(perimetro_triangulo))

    else:
        Area_trapezio = ((a + b) / 2) * c
        print('Area = {:.1f}'.format(Area_trapezio))
