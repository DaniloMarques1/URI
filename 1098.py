i = 0
j = 1
while i <= 2:
	temp = j
	while temp <= j + 2:
		print("I={} J={}".format(i, temp + i))
		temp += 1
	i = round(i + 0.2,1)
	if i % 2 == 1 or i % 2 == 0:
		i = int(i)
		
	
	 	