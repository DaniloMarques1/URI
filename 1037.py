valor = float(input())

if valor < 0 or valor > 100:
	print("Fora de intervalo")
else:
	if valor <= 25:
		print("Intervalo [0,25]")	
	elif valor <= 50:
		print("Intervalo (25,50]")
	elif valor <= 75:
		print("Intervalo (50,75]")
	elif valor <= 100:
		print("Intervalo (75,100]")