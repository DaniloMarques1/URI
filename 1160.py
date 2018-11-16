flag = int(input())

for i in range(0, flag):
	anos = 0
	#pegando a população de cada cidade e a taxa de crescimento
	popA, popB, taxaA,taxaB = map(float, input().split())
	while popA <= popB:
		anos += 1
		#aumentando a população de acordo com a taxa de crescimento
		popA = int(popA * (1 + taxaA / 100))
		popB = int(popB * (1 + taxaB / 100))
		if anos > 100:
			saida = "Mais de 1 seculo."
			break
			
	if anos <= 100:
		saida = "{} anos.".format(anos)
	print(saida)					