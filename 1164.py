x = int(input())
while x > 0:
	l1 = []
	n = int(input())
	for i in range(1, n):
		if n % i == 0:
			l1.append(i)
	if sum(l1) == n:
		print("{} eh perfeito".format(n))
	else:
		print("{} nao eh perfeito".format(n))
	x -= 1				