dia_i = input().split()
hora_i = input().split()
dia_f = input().split()
hora_f = input().split()

hi, mi, si = int(hora_i[0]), int(hora_i[2]), int(hora_i[4])
hf, mf, sf = int(hora_f[0]), int(hora_f[2]), int(hora_f[4])
di, df = int(dia_i[1]), int(dia_f[1])

minuto = 60
hora = minuto * 60
dia = hora * 24

i = si + mi * minuto + hi * hora + di * dia
f = sf + mf * minuto + hf * hora + df * dia

if i < f:
    tempo = f - i
    dias = int(tempo / dia)
    tempo = tempo % dia
    horas = int(tempo / hora)
    tempo = tempo % hora
    minutos = int(tempo / minuto)
    tempo = tempo % minuto
    segundos = tempo
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
