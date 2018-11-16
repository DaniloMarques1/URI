#quantidade de casos
flag = int(input())

for i in range(flag):
	#pegando o nome das duas pessoas a jogar e quem vai ser o par e o impar
	nome1, cond1, nome2, cond2 = input().split()
	n1, n2 = map(int, input().split())
	
	#se for par
	if (n1 + n2) % 2 == 0:
		#definir qual das pessoas ganhou
		if cond1.lower() == "par":
			print(nome1)
		else:
			print(nome2)
	else:
		#se for impar definir qual das pessoas ganhou
		if cond1.lower() == "impar":
			print(nome1)
		else:
			print(nome2)				