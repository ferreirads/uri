x = int(input())

ano = x // 365
y = x % 365
mes = y // 30
dias = y % 30

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dias))
