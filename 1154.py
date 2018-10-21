n = int(input())
l1 = []
while n > 0:
	l1.append(n)
	n = int(input())
media = sum(l1) / len(l1)	
print("{:.2f}".format(media))	