flag = int(input())

for i in range(flag):
	ano = int(input())
	saida = 2015 - ano
	if saida <= 0:
		print("{} A.C.".format(abs(saida) + 1 ))
	else:
		print("{} D.C.".format(abs(saida) ))	
	