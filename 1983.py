flag = int(input())
nota_maior = 0
for i in range(flag):
	matricula, nota = map(float, input().split())
	if nota > nota_maior:
		nota_maior = nota
		saida = int(matricula)

if nota_maior < 8:
	print("Minimum note not reached")
else:
	print(saida)		