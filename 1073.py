#imprimindo o quadrado dos pares ate n
n = int(input())
for i in range(2, n + 1, 2):
	print("{}^2 = {}".format(i, i * i))
