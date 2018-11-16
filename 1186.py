saida = 0
contador = 0
operacao = input()

for linha in range(11, -1, -1):
	for coluna in range(0, 12):
		n = float(input())
		if coluna > linha:
			saida += n
			contador += 1

if operacao == "M":
	saida = saida / contador

print("{:.1f}".format(saida))				