#Achando raizes de uma equação do segundo grau

import math
values = input().split()
a,b,c = values
a = float(a)
b = float(b)
c = float(c)

delta = (b ** 2) - (4 * a * c)
if delta < 0 or a < 1:
	print("Impossivel calcular")
else:
	r1 = (-b + math.sqrt(delta)) / (2 * a)
	r2 = (-b - math.sqrt(delta)) / (2 * a)
	print("R1 = {:.5f}".format(r1))
	print("R2 = {:.5f}".format(r2))