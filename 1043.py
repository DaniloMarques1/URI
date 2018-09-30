a,b,c = map(float, input().split())
if (a < b + c) and (b < a + c) and (c < b + a):
	res = "Perimetro = {}".format(a + b + c)
else:
	res = "Area = {}".format(((a + b) * c) / 2)

print(res)		