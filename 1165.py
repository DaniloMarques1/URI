flag = int(input())
while flag > 0:
	n = int(input())
	divisores = 0
	for i in range(1,n + 1):
		if n % i == 0:
			divisores += 1
	if divisores == 2:
		print("{} eh primo".format(n))
	else:
		print("{} nao eh primo".format(n))
	flag -= 1				