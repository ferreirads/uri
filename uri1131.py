partidas = 0
ponto_inter = 0
ponto_gremio = 0
empate = 0
while True:
    inter, gremio = map(int, input().split())
    partidas = partidas + 1
    if inter > gremio:
        ponto_inter = ponto_inter + 1
    elif inter < gremio:
        ponto_gremio = ponto_gremio + 1
    elif gremio == inter:
        empate = empate + 1
    print('Novo grenal (1-sim 2-nao)')
    novo_grenal = int(input())
    while novo_grenal != 2 and novo_grenal != 1:
        print('Novo grenal (1-sim 2-nao)')
        novo_grenal = int(input())
    if novo_grenal == 2:
        break

print('{} grenais'.format(partidas))
print('Inter:{}'.format(ponto_inter))
print('Gremio:{}'.format(ponto_gremio))
print('Empates:{}'.format(empate))

if ponto_inter > ponto_gremio:
    print('Inter venceu mais')
elif ponto_inter < ponto_gremio:
    print('Gremio venceu mais')
elif ponto_inter == ponto_gremio:
    print('Nao houve vencedor')
