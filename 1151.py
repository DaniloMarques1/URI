a = 0
b = 1
n = int(input())
print("{} {} ".format(a,b),end="")
for i in range(0, n - 2):
	prox = a + b
	if i == n - 3:
		print("{}".format(prox))
	else:
		print("{} ".format(prox),end="")
	a,b = b, a + b			