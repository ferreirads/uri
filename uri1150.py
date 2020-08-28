x = int(input())

while True:
    z = int(input())
    if z > x:
        break
soma = 0
cont = 0
soma2 = 0
while True:
    x = x + soma
    soma = 1
    soma2 = soma2 + x
    cont = cont + 1
    if soma2 > z:
        print(cont)
        break
