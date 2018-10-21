flag = int(input())
p1 = 2
p2 = 3
p3 = 5
while flag > 0:
	n1,n2,n3 = map(float,input().split())
	media = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)
	print("{:.1f}".format(media))
	flag -= 1