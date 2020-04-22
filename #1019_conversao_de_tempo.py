segundos_totais = int(input())

horas = segundos_totais // 3600
horas_aux = segundos_totais % 3600

minutos = horas_aux // 60
minutos_aux = horas_aux % 60

segundos_restantes = minutos_aux

print(horas,minutos,segundos_restantes,sep =':')