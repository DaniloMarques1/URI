def fib(n):
	a,b = 0, 1
	while n > 0:
		a,b = b, a + b
		n -= 1
	return a	
flag = int(input())
while flag > 0:
	n = int(input())
	print("Fib({}) = {}".format(n,fib(n)))
	flag -= 1				

