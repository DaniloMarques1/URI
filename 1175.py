flag = 20
l = []
while flag > 0:
	n = int(input())
	l.append(n)
	flag -= 1
l.reverse()
for i in range(0, len(l)):
	print("N[{}] = {}".format(i, l[i]))	