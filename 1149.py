a,n = [int(x) for x in input().split() if int(x) > 0]
somar = 0
for i in range(a, a + n):
	somar += i
print(somar)	