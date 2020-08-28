n = int(input())
coelho = 0
rato = 0
sapo = 0
total = 0
quantidade = 1
while n > 0 and 1 <= quantidade <= 15:
    quantidade, identificacao = input().split()
    quantidade = int(quantidade)
    identificacao = str(identificacao)
    if identificacao == 'C':
        coelho = quantidade + coelho
    elif identificacao == 'R':
        rato = quantidade + rato
    elif identificacao == 'S':
        sapo = quantidade + sapo
    total = quantidade + total
    n = n - 1

percentual_coelho = (coelho * 100) / total
percentual_rato = (rato * 100) / total
percentual_sapo = (sapo * 100) / total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {percentual_coelho:.2f} %')
print(f'Percentual de ratos: {percentual_rato:.2f} %')
print(f'Percentual de sapos: {percentual_sapo:.2f} %')
