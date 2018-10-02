
x,y = map(float,input().split())

if x == 0 and y == 0:
	pos = "Origem"
elif x == 0:
	pos = "Eixo Y"
elif y == 0:
	pos = "Eixo X"
else:
	if x > 0  and y > 0:
		pos = "Q1"
	elif x < 0 and y > 0:
		pos = "Q2"
	elif x < 0:
		pos = "Q3"
	elif x > 0:
		pos = "Q4"

print(pos)					

