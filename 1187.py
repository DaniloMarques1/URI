#define a operacao
operacao = input()
#somando os valores
saida = 0
#contando para poder saber quantos valores dividir por
contador = 0
#range de colunas que serão adicionadas
coluna_inicial = 1
coluna_final = 10
for linha in range(0,12):
	for coluna in range(0,12):
		n = float(input())
		if coluna >= coluna_inicial and coluna <= coluna_final:
			saida += n
			contador += 1
	coluna_inicial += 1
	coluna_final -= 1

if operacao == "M":
	saida = saida / contador

print("{:.1f}".format(saida))				