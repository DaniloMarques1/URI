x,y = map(int, input().split())
temp = 1
while temp <= y:
	for i in range(0, x - 1):
		if temp >= y:
			break
		print("{} ".format(temp),end="")	
		temp += 1
	print(temp)	
	temp += 1
			
