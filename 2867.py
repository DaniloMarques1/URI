n = int(input())
while n > 0:
	x,y = map(int, input().split())
	digits = len(str(x ** y))
	print(digits)
	n -= 1