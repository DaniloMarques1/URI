print(end="")
a,n = map(int, input().split())
while n <= 0:
	n = int(input())
somar = 0
for i in range(a, a + n):
	somar += i
print(somar)	