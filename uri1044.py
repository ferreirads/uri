A, B = input().split()
A = int(A)
B = int(B)
C = A % B
D = B % A
if C == 0 or D == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
