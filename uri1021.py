A = float(input())

A += 0.001

if 0 <= A <= 1000000.00:
    print('NOTAS:')

    B = A // 100.00
    print('{:.0f} nota(s) de R$ 100.00'.format(B))
    C = A % 100.00

    D = C // 50.00
    print('{:.0f} nota(s) de R$ 50.00'.format(D))
    E = C % 50.00

    F = E // 20.00
    print('{:.0f} nota(s) de R$ 20.00'.format(F))
    G = E % 20.00

    H = G // 10.00
    print('{:.0f} nota(s) de R$ 10.00'.format(H))
    I = G % 10.00

    J = I // 5
    print('{:.0f} nota(s) de R$ 5.00'.format(J))
    K = I % 5.00

    L = K // 2.00
    print('{:.0f} nota(s) de R$ 2.00'.format(L))
    M = K % 2.00

    print('MOEDAS:')

    N = M // 1.00
    print('{:.0f} moeda(s) de R$ 1.00'.format(N))
    O = M % 1.00

    P = O // 0.50
    print('{:.0f} moeda(s) de R$ 0.50'.format(P))
    Q = O % 0.50

    R = Q // 0.25
    print('{:.0f} moeda(s) de R$ 0.25'.format(R))
    S = Q % 0.25

    U = S // 0.10
    print('{:.0f} moeda(s) de R$ 0.10'.format(U))
    V = S % 0.10

    W = V // 0.05
    print('{:.0f} moeda(s) de R$ 0.05'.format(W))
    Y = V % 0.05

    X = Y // 0.01
    print('{:.0f} moeda(s) de R$ 0.01'.format(X))
