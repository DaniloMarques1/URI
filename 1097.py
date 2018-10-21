i = 1
j = 7
while i <= 9:
	temp = j
	while temp >= j - 2:
		print("I={} J={}".format(i,temp))
		temp -= 1
		
	j += 2
	i += 2		
