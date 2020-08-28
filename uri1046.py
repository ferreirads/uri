h_inicial, h_final = input().split()
h_inicial = int(h_inicial)
h_final = int(h_final)

um_dia = 24

if h_inicial > h_final:
    tempo_1 = um_dia - h_inicial
    tempo_jg = tempo_1 + h_final
    print('O JOGO DUROU {} HORA(S)'.format(tempo_jg))
elif h_inicial == h_final:
    print('O JOGO DUROU {} HORA(S)'.format(um_dia))
elif h_inicial < h_final:
    tempo_jg = h_final - h_inicial
    print('O JOGO DUROU {} HORA(S)'.format(tempo_jg))
