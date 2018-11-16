a, b = map(int, input().split())

q = 0

if a >= b:
	while a >= b:
		a = a - b
		q += 1
else:
	while a < b:
		a = a + b
		q += 1 	
r = a
print(q, r)	