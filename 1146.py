x = int(input())
while x != 0:
	for i in range(1, x+1):
		if i == x:
			print("{}".format(i))
		else:
			print("{} ".format(i),end="")
	x = int(input())	