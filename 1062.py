l1 = []
n1 = float(input())
if n1 > 0:
	l1.append(n1)
n2 = float(input())
if n2 > 0:
	l1.append(n2)
n3 = float(input())
if n3 > 0:
	l1.append(n3)
n4 = float(input())
if n4 > 0:
	l1.append(n4)
n5 = float(input())
if n5 > 0:
	l1.append(n5)
n6 = float(input())
if n6 > 0:
	l1.append(n6)
print("{} valores positivos".format(len(l1)))
print("{:.1f}".format(sum(l1) / len(l1)))	