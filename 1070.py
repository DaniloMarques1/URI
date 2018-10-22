#imprimir os 6 valores impares ate X

x = int(input())
cont = 0
while cont < 6:
	if x % 2 != 0:
		print(x)
		cont += 1
	x += 1	
