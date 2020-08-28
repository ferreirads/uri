primeiro_numero = 0
ultimo_numero = 1
fibo = [primeiro_numero, ultimo_numero]

x = int(input())
for i in range(2, x):
    p = primeiro_numero + ultimo_numero
    primeiro_numero = ultimo_numero
    ultimo_numero = p
    fibo.append(p)
print(' '.join(map(str, fibo)))
