inter = 0
gremio = 0
empate = 0
while True:
	x,y = map(int, input().split())
	if x > y:
		inter += 1
	elif x < y:
		gremio += 1
	else:
		empate += 1
	flag = int(input("Novo grenal (1-sim 2-nao)\n"))
	if flag == 2:
		break
if gremio > inter:
	venc = "Gremio venceu mais"	
elif inter > gremio:
	venc = "Inter venceu mais"
else:
	venc = "Não houve vencedor"
print("{} grenais".format(inter + gremio + empate))			
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empate))
print(venc)				