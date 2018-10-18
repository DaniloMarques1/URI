n = int(input())
number_in = 0
number_out = 0
while n > 0:
	x = int(input())
	if x >= 10 and x <= 20:
		number_in += 1
	else:
		number_out += 1
	n -= 1	
print("{} in".format(number_in))
print("{} out".format(number_out))			