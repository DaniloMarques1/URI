even = []
odd = []
for i in range(0, 15):
	n = int(input())
	if n % 2 == 0:
		even.append(n)
	else:
		odd.append(n)
	if len(even) == 5:
		for i in range(len(even)):
			print("par[{}] = {}".format(i, even[i]))
		even = []
	if len(odd) == 5:
		for i in range(len(odd)):
			print("impar[{}] = {}".format(i, odd[i]))
		odd = []	

for i in range(len(odd)):
	print("impar[{}] = {}".format(i, odd[i]))

for i in range(len(even)):
			print("par[{}] = {}".format(i, even[i]))								