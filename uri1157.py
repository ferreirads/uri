n = int(input())
cont = 0
for i in range(n):
    cont = cont + 1
    if n % cont == 0:
        print(cont)
