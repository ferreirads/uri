nome = str(input())
salario = float(input())
totvendas = float(input())

X = (totvendas * 15)/100

Y = salario + X

print('TOTAL = R$ {:.2f}'.format(Y))
