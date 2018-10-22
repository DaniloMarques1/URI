flag = 10
l1 = []
while flag > 0:
	n = int(input())
	l1.append(n)
	flag -= 1
for i in range(0, len(l1)):
	if l1[i] <= 0:
		l1[i] = 1
	print("X[{}] = {}".format(i,l1[i]))			