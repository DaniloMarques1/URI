flag = 100
l = []
while flag > 0:
	n = float(input())
	l.append(n)
	flag -= 1
for i in range(0, len(l)):
	if l[i] <= 10:
		print("A[{}] = {:.1f}".format(i,l[i]))	