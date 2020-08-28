n = int(input())
numero = 0
if 1 < n < 1000:
    for i in range(n):
        numero = numero + 1
        a = numero ** 2
        b = numero ** 3
        print(f'{numero} {a} {b}')

