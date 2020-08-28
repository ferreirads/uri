salario = float(input())

if 0 < salario <= 2000.00:
    print('Isento')

elif 2000.00 < salario <= 3000.00:
    a = salario - 2000
    b = (a * 8) / 100
    print('R$ {:.2f}'.format(b))

elif 3000.00 < salario <= 4500.00:
    a = salario - 2000
    b = a - 1000
    c = (1000 * 8) / 100
    d = (b * 18) / 100
    e = c + d
    print('R$ {:.2f}'.format(e))

else:
    a = salario - 2000
    b = a - 1000
    c = (1000 * 8) / 100
    d = b - 1500
    e = (1500 * 18) / 100
    f = (d * 28) / 100
    g = f + c + e
    print('R$ {:.2f}'.format(g))
