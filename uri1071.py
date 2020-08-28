n1 = int(input())
n2 = int(input())
soma = 0
for i in range(n2 + 1, n1):
    if i % 2 != 0:
        soma = soma + i
print(soma)
