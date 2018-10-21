x = int(input())
while x != 0:
	if x % 2 == 1:
		x += 1
	flag = 5
	somador = 0
	while flag > 0:
		somador += x
		x += 2
		flag -= 1
	print(somador)
	x = int(input())	