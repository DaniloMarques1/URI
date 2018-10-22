n = int(input())
temp = 0
l = []
for i in range(0, 1000):
	l.append(temp)
	print("N[{}] = {}".format(i,l[i]))
	temp += 1
	if temp  == n:
		temp = 0
		