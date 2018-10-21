n = int(input())
while n > 0:
	x,y = map(int, input().split())
	if x % 2 == 0:
		x = x + 1
	total = 0
	while y > 0:
		total += x
		x += 2
		y -= 1
	print(total)
	n -= 1	