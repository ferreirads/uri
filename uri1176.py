T = int(input())

for i in range(T):
    n = int(input())
    p = 0
    u = 1
    fib = [p, u]
    for j in range(2, n + 1):
        a = p + u
        p = u
        u = a
        fib.append(a)
    print('Fib({}) = {}'.format(n, fib[n]))
