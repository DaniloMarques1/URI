x = int(input())
z = int(input())
while z <= x:
	z = int(input())
contador = 0
somador = 0
for i in range(x,z):
	if somador > z:
		break
	somador = somador + i
	contador += 1
print(contador)	