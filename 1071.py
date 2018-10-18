x = int(input())
y = int(input())
totImpar = 0
for i in range(y + 1,x):
	if i % 2 != 0:
		totImpar += i
print(totImpar)		