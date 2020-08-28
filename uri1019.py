x = int(input())

horas = x // 3600
y = x % 3600
minutos = y // 60
segundos = y % 60

print('{}:{}:{}'.format(horas, minutos, segundos))