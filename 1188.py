operacao = input()
saida = 0
contador = 0

coluna_inicial = 4
coluna_final = 7
linha_inicial = 7

for linha in range(0, 12):
	for coluna in range(0, 12):
		n = float(input())
		#se chegarmos na linha que vamos iniciar as somas
		if linha >= linha_inicial:
			if coluna > coluna_inicial and coluna < coluna_final:
				saida += n
				contador += 1	 
	#caso ja tenhamos chegando na linha em que a soma acontecera expadir as colunas
	if linha >= linha_inicial:
		coluna_inicial -= 1
		coluna_final += 1

if operacao == "M":
	saida = saida / contador

print("{:.1f}".format(saida))			