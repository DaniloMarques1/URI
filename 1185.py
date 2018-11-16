saida = 0
#contar os numeros que foram adicionados
operacao = input()
contador = 0
for linha in range(0, 12):
	for coluna in range(11, -1, -1):
		n = float(input())
		if coluna > linha:
			saida += n
			contador += 1
if operacao == "M":
	saida = saida / contador

print("{:.1f}".format(saida))				
