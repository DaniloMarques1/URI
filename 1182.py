#Ler 12 numeros em 12 arrays e receber duas entradas, uma em qual coluna realizar uma determinada operação e na outra a operação a ser realizaa (Media ou soma)
l = []
soma = 0
#coluna
c = int(input())
#operação
s = input()
for arr in range(12):
	for element in range(12):
		n = float(input())
		if element == c:
			soma += n
if s == "M":
	saida = soma / 12
else:
	saida = soma	 			
print("{:.1f}".format(saida))	