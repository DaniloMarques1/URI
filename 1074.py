flag = int(input())
while flag > 0:
	n = int(input())
	if n % 2 == 0:
		if n > 0:
			print("EVEN POSITIVE")
		elif n < 0:
			print("EVEN NEGATIVE")
		else:
			print("NULL")
	else:
		if n > 0:
			print("ODD POSITIVE")
		else:
			print("ODD NEGATIVE")
	flag -= 1			