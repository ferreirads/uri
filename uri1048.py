salario = float(input())

if 0 < salario <= 400.00:
    porcentagem = 15
    nov_salario = salario * 1.15
    reajuste = nov_salario - salario

elif 400.00 < salario <= 800.00:
    porcentagem = 12
    nov_salario = salario * 1.12
    reajuste = nov_salario - salario

elif 800.00 < salario <= 1200.00:
    porcentagem = 10
    nov_salario = salario * 1.10
    reajuste = nov_salario - salario

elif 1200.00 < salario <= 2000.00:
    porcentagem = 7
    nov_salario = salario * 1.07
    reajuste = nov_salario - salario

elif 2000.00 < salario:
    porcentagem = 4
    nov_salario = salario * 1.04
    reajuste = nov_salario - salario

print('Novo salario: {:.2f}'.format(nov_salario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(porcentagem))
