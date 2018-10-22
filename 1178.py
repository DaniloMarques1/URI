n = float(input())
l = []
for i in range(0, 100):
	l.append(n)
	print("N[{}] = {:.4f}".format(i,l[i]))
	n = n / 2	