l = []
#sub array que a operação vai ser executada
n = int(input())
#A operação
s = input()
for i in range(0, 12):
	#recebendo o sub array em uma linha
	sub = []
	for i in range(0 , 12):
		valor = float(input())
		sub.append(valor)
	l.append(sub)	

#escolhendo a operação
if s == "S":
	saida = sum(l[n])
elif s == "M":
	saida = ((sum(l[n])) / 12)

print("{:.1f}".format(saida))

