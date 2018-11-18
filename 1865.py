flag = int(input())
for i in range(flag):
	heroi, forca = input().split()
	if heroi.lower() == "thor":
		print("Y")
	else:
		print("N")	