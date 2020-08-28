alcool = 0
gasolina = 0
diesel = 0
while True:
    combustivel = int(input())
    if combustivel == 1:
        alcool = alcool + 1
    elif combustivel == 2:
        gasolina = gasolina + 1
    elif combustivel == 3:
        diesel = diesel + 1
    elif combustivel == 4:
        break

print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(alcool, gasolina, diesel))
