while True:
	x,y = map(int,input().split())
	if x <= 0 or y <= 0:
		break
	if x > y:
		maior = x
		menor = y
	else:
		maior = y
		menor = x
	soma = 0
	for i in range(menor,maior + 1):
		print("{} ".format(i),end="")
		soma += i
	print("Sum={}".format(soma))
