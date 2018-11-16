t = list(map(int, input().split()))
if sum(t) < 3:
	print("N")
else:	
	copia = t.copy()
	copia.remove(max(copia))


	if (copia[0] < copia[1] + copia[2]) and (copia[1] < copia[0] + copia[2] ) and (copia[2] < copia[1] + copia[0]):
		saida1 = "S"
	else:
		saida1 = "N"	

	copia = t.copy()
	copia.remove(min(copia))

	if (copia[0] < copia[1] + copia[2]) and (copia[1] < copia[0] + copia[2] ) and (copia[2] < copia[1] + copia[0] ):
		saida2 = "S"
	else:
		saida2 = "N"


	if saida1 == saida2:
		print(saida1)
	else:
		print("S")			
