flag = int(input())
while flag > 0:
	x,y = map(int, input().split())
	soma = 0
	if x > y:
		maior = x
		menor = y
	else:
		maior = y
		menor = x
	for i in range(menor + 1 , maior):		
		if i % 2 != 0:
			soma += i
	print(soma)
	flag -= 1		