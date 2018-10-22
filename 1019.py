#Recebendo o tempo em segundos e exibindo em horas:minutos:segundos
tempo_seg = int(input())

horas = tempo_seg // 3600

resto = tempo_seg % 3600

minutos = resto // 60
segundos = resto % 60

print("{}:{}:{}".format(horas,minutos,segundos)) 