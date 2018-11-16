#Operação acima da diagonal principal de uma matriz
saida = 0
#contar quantos numeros estão sendo somados para realizar a media caso essa seja a operação a ser realizada
contador = 0
operacao = input()
#linhas
for linha in range(0, 12):
	#colunas
	for coluna in range(0,12):
		n = float(input())
		if coluna > linha:
			#adicionar apenas as colunas que estejam acima da linha
			saida += n
			contador += 1
			
if operacao == "M":
	saida = saida / contador

print("{:.1f}".format(saida))				