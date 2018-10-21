n = int(input())
contador = 1
while n > 0:
	for i in range(0,3):
		print("{} ".format(contador),end="")
		contador += 1
	print("PUM")
	contador += 1
	n -= 1	