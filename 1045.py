#Recebe 3 valores verifica se forma um triangulo e que tipo de triangulo é

a,b,c = sorted(map(float,input().split()), reverse = True)

if (a >= b + c) or (b >= a + c) or (c >= a + b):
	print("NAO FORMA TRIANGULO")
else:
	if (a ** 2) == (b ** 2 + c ** 2):
		print("TRIANGULO RETANGULO")
	elif (a ** 2) > (b ** 2 + c ** 2):
		print("TRIANGULO OBTUSANGULO")
	elif (a ** 2) < (b ** 2 + c ** 2):
		print("TRIANGULO ACUTANGULO")

if a == b and a == c:
	print("TRIANGULO EQUILATERO")
elif a == b or a == c or c == b:
	print("TRIANGULO ISOSCELES")					
