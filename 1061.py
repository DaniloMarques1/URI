
temp, diaI = input().split()
diaI = int(diaI)
horasI, minutosI,segundosI = map(int, input().split(":"))

temp, diaf = input().split()
diaf = int(diaf)
horasf,minutosf, segundosf = map(int, input().split(":"))

horasinicial = (diaI * 24 * 60 * 60) + (horasI * 60 * 60) + (minutosI * 60) + segundosI

horasfinal = (diaf * 24 * 60 * 60) + (horasf * 60 * 60) + (minutosf * 60) + segundosf

segundosTotal = horasfinal - horasinicial

dias = segundosTotal // 86400
resto = segundosTotal % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
resto = resto % 60

print("{} dia(s)".format(dias))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(resto))