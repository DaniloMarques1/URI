values = input().split()
a,b,c = values
maiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2

if maiorAB > int(c):
	print(int(maiorAB), "eh o maior")
else:
	print(int(c), "eh o maior")	