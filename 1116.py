'''flag = int(input())
while flag > 0:
	x,y = map(int, input().split())
	try:
		print("{:.1f}".format(x / y))
	except ZeroDivisionError:
		print("divisao impossivel")
	flag -= 1	'''
flag = int(input())
while flag > 0:
	x,y = map(int, input().split())
	if x == 0 or y == 0:
		print("divisao impossivel")	