flag = int(input())
for i in range(flag):
	n = -1
	numero = int(input())
	somador = 1
	for i in range(numero + 1):
		somador = somador + n
		n = n * -1
	print(somador)	
