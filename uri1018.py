a = int(input())

print(a)

if 0 < a < 1000000:

    b = a // 100
    print('{} nota(s) de R$ 100,00'.format(b))
    c = a % 100

    d = c // 50
    print('{} nota(s) de R$ 50,00'.format(d))
    e = c % 50

    f = e // 20
    print('{} nota(s) de R$ 20,00'.format(f))
    g = e % 20

    h = g // 10
    print('{} nota(s) de R$ 10,00'.format(h))
    i = g % 10

    j = i // 5
    print('{} nota(s) de R$ 5,00'.format(j))
    k = i % 5

    l = k // 2
    print('{} nota(s) de R$ 2,00'.format(l))
    m = k % 2

    n = m // 1
    print('{} nota(s) de R$ 1,00'.format(n))

else:
    EOFError
